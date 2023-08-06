"""
Various utility functions that can be used internally either by the client-side
or the service-side.
"""

from qwilprobe.generated.qwilprobe_pb2 import ProbeDataType


def datatype_to_string(datatype):
    return ProbeDataType.Name(datatype)

def check_datatype(datatype):
    """
    Check if an integer/enum is within the range that the qwilprobe proto file
    allows.
    """

    try:
        # Attempt to access name of enum elem in qwilbrobe.proto by given info.
        ProbeDataType.Name(datatype)
    except (ValueError, TypeError):
        # Fails if given info is not an integer within the enum range
        return False

    return True
