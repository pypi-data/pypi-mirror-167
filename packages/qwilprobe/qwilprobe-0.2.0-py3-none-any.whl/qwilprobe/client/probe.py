"""
Main module for creating qwilprobe clients (a.k.a. Probes)
"""

import grpc

from qwilprobe.generated.qwilprobe_pb2 import (
    ProbeDataRequest,
    ProbeDataResponse,
    ProbeDataType,
    ProbeInfoRequest,
    ProbeInfoResponse,
    ProbeIsReadyRequest,
    ProbeIsReadyResponse,
    ProbeTerminateRequest,
)
from qwilprobe.generated.qwilprobe_pb2_grpc import QwilprobeStub
from qwilprobe.shared.constants import (
    DEFAULT_ADDRESS,
    DEFAULT_PORT,
    KEY_COLINFO,
    KEY_COLINFO_DESCR,
    KEY_COLINFO_NAME,
    KEY_COLINFO_TYPE,
    KEY_DESCR,
    KEY_UID,
)


class Probe:
    """
    Class for instantiating microservice clients.
    """

    def __init__(self,
                 service_uid=None,
                 address=DEFAULT_ADDRESS,
                 port=DEFAULT_PORT):
        """
        Contructor for the Probe class.
        :param str service_uid: Optional. Expected UID by the service. If
            provided, the Probe instance (client) will raise an error if
            the service presents something different.
        :param str address: Optional. Default "localhost".
        :param int port: Optional. Default 30051.
        """
        self.service_uid = service_uid
        self.channel = grpc.insecure_channel(f"{address}:{str(port)}")
        self.stub = QwilprobeStub(self.channel)

    def get_probe_info(self):
        """
        Get the probe info from the service. Do some very basic checks
        and then return it as a python dict. TODO stricter checks?
        """
        probe_info_raw = self.stub.GetProbeInfo(ProbeInfoRequest())
        probe_info = {}

        if probe_info_raw.uid:
            probe_info[KEY_UID] = probe_info_raw.uid
        else:
            self.channel.close()
            raise ValueError("Service did not present an UID!")

        if self.service_uid and probe_info_raw.uid != self.service_uid:
            self.channel.close()
            raise ValueError(f"Unexpected service found: {probe_info_raw.uid}")

        if (not probe_info_raw.data_model or
           not probe_info_raw.data_model.columns):
            self.channel.close()
            raise ValueError("Empty or no data model provided!")

        probe_info[KEY_COLINFO] = []
        for c in probe_info_raw.data_model.columns:
            column_info = {}
            column_info[KEY_COLINFO_NAME] = c.column_name
            column_info[KEY_COLINFO_TYPE] = c.column_type
            column_info[KEY_COLINFO_DESCR] = c.column_description
            probe_info[KEY_COLINFO].append(column_info)

        probe_info[KEY_DESCR] = probe_info_raw.description

        return probe_info

    def get_probe_is_ready(self):
        """
        Check whether the service is ready or not. Returns True or False.
        """
        probe_is_ready_raw = self.stub.GetProbeIsReady(ProbeIsReadyRequest())
        return probe_is_ready_raw.is_ready

    def get_probe_data(self):
        """
        Get a measurement from the probe. Returns data in key-value pairs
        where the keys are the column names as presented by ``get_probe_info``.
        """
        probe_data_raw = self.stub.GetProbeData(ProbeDataRequest())
        probe_data = {}
        if not probe_data_raw.probe_data:
            raise ValueError("No data in response!")

        for d in probe_data_raw.probe_data:
            if not d.key:
                raise ValueError("A datapoint is missing a key!")
            if not d.WhichOneof("value"):
                raise ValueError("A datapoint is missing a value!")
            probe_data[d.key] = getattr(d,
                                        d.WhichOneof("value"))
        return probe_data

    def terminate(self):
        """
        Request the server to terminate and close the channel.
        """
        response = self.stub.Terminate(ProbeTerminateRequest())
        self.channel.close()
        return response
