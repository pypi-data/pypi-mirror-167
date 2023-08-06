##################### START BOILERPLATE ####################################################

from ..stubs_grpcio import system_api_pb2
from ..stubs_grpcio import common_pb2
from ..stubs_grpcio import network_api_pb2
import remotivelabs.broker.sync as broker
import os

import hashlib
import posixpath
import ntpath
import itertools
import grpc

from urllib.parse import urlparse
from grpc_interceptor import ClientCallDetails, ClientInterceptor
from typing import Any, Callable


class HeaderInterceptor(ClientInterceptor):
    def __init__(self, header_dict):
        self.header_dict = header_dict

    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        call_details: grpc.ClientCallDetails,
    ):
        new_details = ClientCallDetails(
            call_details.method,
            call_details.timeout,
            self.header_dict.items(),
            call_details.credentials,
            call_details.wait_for_ready,
            call_details.compression,
        )

        return method(request_or_iterator, new_details)


def create_channel(url, x_api_key):

    url = urlparse(url)

    if url.scheme == "https":
        creds = grpc.ssl_channel_credentials(
            root_certificates=None, private_key=None, certificate_chain=None
        )
        channel = grpc.secure_channel(
            url.hostname + ":" + str(url.port or "443"), creds
        )
    else:
        channel = grpc.insecure_channel(url.hostname + ":" + str(url.port or "50051"))

    intercept_channel = grpc.intercept_channel(
        channel, HeaderInterceptor({"x-api-key": x_api_key})
    )
    return intercept_channel


def publish_signals(client_id, stub, signals_with_payload, frequency=0):
    """Publish signals

    Parameters
    ----------
    client_id : ClientId
        Object instance of class
    stub : NetworkServiceStub
        Object instance of class
    signals_with_payload : Signal
        Object instance of class

    """
    publisher_info = network_api_pb2.PublisherConfig(
        clientId=client_id,
        signals=network_api_pb2.Signals(signal=signals_with_payload),
        frequency=frequency,
    )
    try:
        stub.PublishSignals(publisher_info)
    except grpc._channel._Rendezvous as err:
        print(err)


def printer(signals):
    for signal in signals:
        print(f"{signal.id.name} {signal.id.namespace.name} {get_value(signal)}")


def get_sha256(file):
    f = open(file, "rb")
    bytes = f.read()  # read entire file as bytes
    readable_hash = hashlib.sha256(bytes).hexdigest()
    return readable_hash


def generate_data(file, dest_path, chunk_size, sha256):
    for x in itertools.count(start=0):
        if x == 0:
            fileDescription = system_api_pb2.FileDescription(
                sha256=sha256, path=dest_path
            )
            yield system_api_pb2.FileUploadRequest(fileDescription=fileDescription)
        else:
            buf = file.read(chunk_size)
            if not buf:
                break
            yield system_api_pb2.FileUploadRequest(chunk=buf)


def upload_file(stub, path, dest_path):
    sha256 = get_sha256(path)
    print(sha256)
    file = open(path, "rb")

    # make sure path is unix style (necessary for windows, and does no harm om linux)
    upload_iterator = generate_data(
        file, dest_path.replace(ntpath.sep, posixpath.sep), 1000000, sha256
    )
    response = stub.UploadFile(upload_iterator, compression=grpc.Compression.Gzip)
    print("uploaded", path, response)


def download_file(stub, path, dest_path):
    file = open(dest_path, "wb")
    for response in stub.DownloadFile(
        system_api_pb2.FileDescription(path=path.replace(ntpath.sep, posixpath.sep))
    ):
        assert response.HasField("errorMessage") == False, (
            "Error uploading file, message is: %s" % response.errorMessage
        )
        file.write(response.chunk)
    file.close()


from glob import glob


def upload_folder(system_stub, folder):
    files = [
        y
        for x in os.walk(folder)
        for y in glob(os.path.join(x[0], "*"))
        if not os.path.isdir(y)
    ]
    assert len(files) != 0, (
        "Specified upload folder is empty or does not exist, provided folder was: %s"
        % folder
    )
    for file in files:
        upload_file(system_stub, file, file.replace(folder, ""))


def reload_configuration(system_stub):
    request = common_pb2.Empty()
    response = system_stub.ReloadConfiguration(request, timeout=60000)
    print(response)


def check_license(system_stub):
    status = system_stub.GetLicenseInfo(common_pb2.Empty()).status
    assert status == system_api_pb2.LicenseStatus.VALID, (
        "Check your license, status is: %d" % status
    )


import requests
import json
import base64

# re-request a license. By default uses the same email (requestId) as before
# hash will be found in your mailbox
def request_license(system_stub, id=None):
    if id == None:
        id = system_stub.GetLicenseInfo(common_pb2.Empty()).requestId
        assert id != "", "no old id available, provide your email"
    requestMachineId = system_stub.GetLicenseInfo(common_pb2.Empty()).requestMachineId
    body = {"id": id, "machine_id": json.loads(requestMachineId)}
    resp_request = requests.post(
        "https://www.beamylabs.com/requestlicense",
        json={
            "licensejsonb64": base64.b64encode(
                json.dumps(body).encode("utf-8")
            ).decode()
        },
    )
    assert (
        resp_request.status_code == requests.codes.ok
    ), "Response code not ok, code: %d" % (resp_request.status_code)
    print("License requested, check your mail: ", id)


# using your hash, upload your license (remove the dashes) use the same email (requestId) address as before
def download_and_install_license(system_stub, hash, id=None):
    if id == None:
        id = system_stub.GetLicenseInfo(common_pb2.Empty()).requestId
        assert id.encode("utf-8") != "", "no old id avaliable, provide your email"
    resp_fetch = requests.post(
        "https://www.beamylabs.com/fetchlicense",
        json={"id": id, "hash": hash.replace("-", "")},
    )
    assert (
        resp_fetch.status_code == requests.codes.ok
    ), "Response code not ok, code: %d" % (resp_fetch.status_code)
    license_info = resp_fetch.json()
    license_bytes = license_info["license_data"].encode("utf-8")
    # you agree to license and conditions found here https://www.beamylabs.com/license/
    system_stub.SetLicense(
        system_api_pb2.License(termsAgreement=True, data=license_bytes)
    )


def act_on_signal(client_id, stub, sub_signals, on_change, fun, on_subcribed=None):
    sub_info = network_api_pb2.SubscriberConfig(
        clientId=client_id,
        signals=network_api_pb2.SignalIds(signalId=sub_signals),
        onChange=on_change,
    )
    try:
        subscripton = stub.SubscribeToSignals(sub_info, timeout=None)
        if on_subcribed:
            on_subcribed(subscripton)
        print("waiting for signal...")
        for subs_counter in subscripton:
            fun(subs_counter.signal)

    except grpc.RpcError as e:
        try:
            subscripton.cancel()
        except grpc.RpcError as e2:
            pass

    except grpc._channel._Rendezvous as err:
        print(err)
    # reload, alternatively non-existing signal
    print("subscription terminated")


##################### END BOILERPLATE ####################################################
