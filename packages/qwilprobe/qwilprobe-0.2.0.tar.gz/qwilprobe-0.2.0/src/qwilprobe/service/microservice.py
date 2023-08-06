"""
Main module for qwilprobe microservices.
"""

import threading
from concurrent import futures

import grpc

from qwilprobe.generated.qwilprobe_pb2 import (
    ProbeDataColumn,
    ProbeDataModel,
    ProbeDataResponse,
    ProbeInfoResponse,
    ProbeIsReadyResponse,
    ProbeTerminateResponse,
)
from qwilprobe.generated.qwilprobe_pb2_grpc import (
    QwilprobeServicer,
    add_QwilprobeServicer_to_server,
)
from qwilprobe.shared.constants import (
    KEY_COLINFO_DESCR,
    KEY_COLINFO_NAME,
    KEY_COLINFO_TYPE,
)


def _default_probe_info_handler():
    """Default handler for GetProbeInfo RPC."""
    print("Calling 'GetProbeInfo'")
    return _probe_info


def _default_probe_is_ready_handler():
    """Default handler for GetProbeIsReady RPC."""
    print("Calling 'GetProbeIsReady'")
    return True


def _default_probe_data_handler():
    """Default handler for GetProbeData RPC."""
    print("Calling 'GetProbeData'")
    return None


def _default_terminate_handler():
    """Default handler for Terminate RPC."""
    print("Calling 'Terminate'")
    return None


_get_probe_info_handler = _default_probe_info_handler
_get_probe_is_ready_handler = _default_probe_is_ready_handler
_get_probe_data_handler = _default_probe_data_handler
_terminate_handler = _default_terminate_handler
_terminate_event = threading.Event()  # For shutting down server
_probe_info = None


def register_get_probe_info_handler(handler):
    global _get_probe_info_handler
    _get_probe_info_handler = handler


def register_get_probe_is_ready_handler(handler):
    global _get_probe_is_ready_handler
    _get_probe_is_ready_handler = handler


def register_get_probe_data_handler(handler):
    global _get_probe_data_handler
    _get_probe_data_handler = handler


def register_terminate_handler(handler):
    global _terminate_handler
    _terminate_handler = handler


def set_probe_info(uid, column_info, description):
    global _probe_info
    # TODO make into a list!

    columns = []
    for c in column_info:
        column = ProbeDataColumn()
        column.column_name = c[KEY_COLINFO_NAME]
        column.column_type = c[KEY_COLINFO_TYPE]
        if KEY_COLINFO_DESCR in c.keys():
            column.column_description = c[KEY_COLINFO_DESCR]

        columns.append(column)

    model = ProbeDataModel(columns=columns)
    probe_info = ProbeInfoResponse(uid=uid, data_model=model)

    if description:
        probe_info.description = description

    _probe_info = probe_info


class _QwilprobeServicer(QwilprobeServicer):
    """Thin wrapper class around the main functionality of this module."""

    def GetProbeInfo(self, request, context):
        retval = _get_probe_info_handler()
        if not retval:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details("No handler for 'GetProbeInfo'")
            return ProbeInfoResponse()

        return retval

    def GetProbeIsReady(self, request, context):
        retval = _get_probe_is_ready_handler()
        if not isinstance(retval, bool):
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details("Unexpected return from 'GetProbeIsReady'")
            return ProbeIsReadyResponse(is_ready=False)

        return ProbeIsReadyResponse(is_ready=retval)

    def GetProbeData(self, request, context):
        raw_data = _get_probe_data_handler()

        if not raw_data:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details(
                "Handler for 'GetProbeData' probably not registered")
            return ProbeDataResponse()

        data_ok, response = _convert_probe_data(raw_data, _probe_info)
        if not data_ok:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details(
                "Handler for 'GetProbeData' returned unexpected data")
            return ProbeDataResponse()

        return response

    def Terminate(self, request, context):
        _terminate_handler()  # Not expecting it to return anything
        _terminate_event.set()
        return ProbeTerminateResponse()


def start(address, port):
    # Clear the terminate event to ensure this thread will block further down
    _terminate_event.clear()

    # Create objects for termination event and gRPC server
    _server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Create the qwilprobe servicer and add it to the gRPC server
    add_QwilprobeServicer_to_server(
        _QwilprobeServicer(), _server)

    # Start the server
    _server.add_insecure_port(address + ":" + str(port))
    _server.start()

    # Block this thread until a handler signals to terminate
    _terminate_event.wait()

    # 1 second grace time then goodbye
    _server.stop(1)


def stop():
    _terminate_event.set()


def _convert_probe_data(data, probe_info_response=None):
    """
    Convert a dict to a ProbeDataResponse. If a ProbeInfoResponse is supplied,
    it will make sure the data adheres to the model within.
    """
    if (probe_info_response and
       isinstance(probe_info_response, ProbeInfoResponse)):
        model = {c.column_name: c.column_type
                 for c in probe_info_response.data_model.columns}

        datapoints = []
        for k, v in data.items():
            if k not in model.keys():
                return False, None

            datapoint = ProbeDatapoint(key=k)

            if model[k] == ProbeDataType.INTEGER:
                try:
                    datapoint.intval = v
                except Exception:
                    return False, None
            elif model[k] == ProbeDataType.REAL:
                try:
                    datapoint.realval = v
                except Exception:
                    return False, None
            elif model[k] == ProbeDataType.STRING:
                try:
                    datapoint.stringval = v
                except Exception:
                    return False, None
            else:
                return False, None

            datapoints.append(datapoint)

        response = ProbeDataResponse(probe_data=datapoints)

    else:  # No probe info given. Attempt to build a ProbeDataResponse anyway
        datapoints = []
        for k, v in data.items():
            if not isinstance(k, str):
                return False, None

            datapoint = ProbeDatapoint(key=k)

            if isinstance(v, int):
                datapoint.intval = v
            elif isinstance(v, float):
                datapoint.realval = v
            elif isinstance(v, str):
                datapoint.stringval = v
            else:
                return False, None

            datapoints.append(datapoint)

        response = ProbeDataResponse(probe_data=datapoints)

    return True, response
