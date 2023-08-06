"""
API for writing probes for the qwilfish fuzzer.
"""

import qwilprobe.service.microservice as qpms
import qwilprobe.shared.constants as constants
import qwilprobe.shared.util as util
from qwilprobe.generated.qwilprobe_pb2 import ProbeDataType

#: Pass to :func:`qwilprobe_register_handler` to register handler for this RPC
RPC_GET_PROBE_INFO = "GetProbeInfo"
#: Pass to :func:`qwilprobe_register_handler` to register handler for this RPC
RPC_GET_PROBE_IS_READY = "GetProbeIsReady"
#: Pass to :func:`qwilprobe_register_handler` to register handler for this RPC
RPC_GET_PROBE_DATA = "GetProbeData"
#: Pass to :func:`qwilprobe_register_handler` to register handler for this RPC
RPC_TERMINATE = "Terminate"

#: Used to indicate the datatype of a column in
#: :func:`qwilprobe_set_probe_info`
DATATYPE_INTEGER = ProbeDataType.INTEGER
#: Used to indicate the datatype of a column in
#: :func:`qwilprobe_set_probe_info`
DATATYPE_REAL = ProbeDataType.REAL
#: Used to indicate the datatype of a column in
#: :func:`qwilprobe_set_probe_info`
DATATYPE_STRING = ProbeDataType.STRING

# Use constants instead of magic strings when accessing dictionary elements
KEY_UID = constants.KEY_UID
KEY_COLINFO = constants.KEY_COLINFO
KEY_DESCR = constants.KEY_DESCR
KEY_COLINFO_NAME = constants.KEY_COLINFO_NAME
KEY_COLINFO_TYPE = constants.KEY_COLINFO_TYPE
KEY_COLINFO_DESCR = constants.KEY_COLINFO_DESCR

def qwilprobe_register_handler(rpc_name, handler):
    """
    Register a handler for various RPCs.

    :param str rpc_name: Required. RPC name to register a handler for.
        Use :const:`RPC_GET_PROBE_INFO`, :const:`RPC_GET_PROBE_IS_READY`,
        :const:`RPC_GET_PROBE_DATA` or :const:`RPC_TERMINATE` for convenience.
    :param handler: Required. Handler function for the specified RPC. Depending
        on ``rpc_name``, the handler is expected to behave differently:

        - For :const:`RPC_GET_PROBE_INFO` the handler should take no input
          parameters and return a dict with these keys:

          - :obj:`"uid" <str>` (Required)
          - :obj:`"column_info" <list>` (Required)
          - :obj:`"description" <str>` (Optional)

          See the parameters for :func:`qwilprobe_set_probe_info` for details
          on what the above keys should map to. Other keys pairs will be
          ignored.

          Default handler will return whatever has been set with
          :func:`qwilprobe_set_probe_info` or raise an exception on the client
          side if nothing has been set.

        - For :const:`RPC_GET_PROBE_IS_READY` the handler should take no input
          parameters and return a :obj:`bool`.

          Default handler will always return :obj:`True <bool>`.

        - For :const:`RPC_GET_PROBE_DATA` the handler should take no input
          parameters and return a :obj:`dict` with column names for keys and
          probe data as values. If probe info has been set using
          :func:`qwilprobe_set_probe_info` the returned :obj:`dict` will be
          checked for correctness (e.g. no undefined column names or type
          mismatches).

          Default handler will raise an exception on the client side.

        - For :const:`RPC_TERMINATE` the handler should take no input
          parameters and return nothing. The main idea is to use it for cleanup
          before shutting down.

          Default handler does nothing.

          `The handler being registered does not need to care about the actual
          shutting down of the service, that will happen regardless`.

    :raise ValueError: If handler is not a callable or if an invalid RPC name
        is supplied.
    :return: None
    """
    if not callable(handler):
        raise ValueError(f"Handler {handler} is not callable!")

    if rpc_name == RPC_GET_PROBE_INFO:
        qpms.register_get_probe_info_handler(handler)
    elif rpc_name == RPC_GET_PROBE_IS_READY:
        qpms.register_get_probe_is_ready_handler(handler)
    elif rpc_name == RPC_GET_PROBE_DATA:
        qpms.register_get_probe_data_handler(handler)
    elif rpc_name == RPC_TERMINATE:
        qpms.register_terminate_handler(handler)
    else:
        raise ValueError(f"No RPC named '{rpc_name}'. Handler not registered.")


def qwilprobe_set_probe_info(uid, column_info, description=None):
    """
    Set the info that will be the response to GetProbeInfo requests (unless a
    non-default handler that does something different has been registered).

    :param str uid: A campaign-wide unique identifier for this service.
                    (Required)
    :param list column_info: A list of dicts that represent the columns in a
                             table where the data will be stored e.g. an SQLite
                             database. The following keys are expected in every
                             element of the list (i.e. every dict):

                             - :obj:`"column_name" <str>` (Required) A name for
                               the column.
                             - :obj:`"column_type" <str>` (Required) Type of
                               data to be stored in the column. Use
                               :const:`DATATYPE_INTEGER`,
                               :const:`DATATYPE_REAL` or
                               :const:`DATATYPE_STRING`.
                             - :obj:`"column_description" <str>` (Optional) A
                               short description about what data will be
                               stored in the column.

    :param str description: A short description of the service.
    """
    if not isinstance(uid, str) or not uid:
        raise ValueError("Probe UID must be a non-empty string!")

    if not isinstance(column_info, list) or not column_info:
        raise ValueError("Column info must be a non-empty list")

    for c in column_info:
        if not isinstance(c, dict) or not c:
            raise ValueError("Column info must be a list of non-empty dicts!")
        if not KEY_COLINFO_NAME in c.keys():
            raise ValueError("Column info must contain a 'column_name' key!")
        if not isinstance(c[KEY_COLINFO_NAME], str) or not c[KEY_COLINFO_NAME]:
            raise ValueError("Column name must be a non-empty string!")
        if not KEY_COLINFO_TYPE in c.keys():
            raise ValueError("Column info must contain a 'column_type' key!")
        if not util.check_datatype(c[KEY_COLINFO_TYPE]):
            raise ValueError("Bad column type!")
        if KEY_COLINFO_DESCR in c.keys():
            if c[KEY_COLINFO_DESCR] is None:
                pass  # None is ok for description value
            if not isinstance(c[KEY_COLINFO_DESCR], str):
                raise ValueError("Column description must be a string!")

    if description:
        if not isinstance(description, str):
            raise ValueError("Make sure probe description is a string!")

    qpms.set_probe_info(uid, column_info, description)


def qwilprobe_start(address=
                    constants.DEFAULT_ADDRESS,
                    port=constants.DEFAULT_PORT):
    qpms.start(address, port)


def qwilprobe_stop():
    qpms.stop()

def qwilprobe_datatype_to_string(datatype):
    """
    Convert a datatype from it's enum/integer to a string representation.

    :param int datatype: Enum/integer representation of datatype 

    :return str
    """
    return util.datatype_to_string(datatype)

def qwilprobe_check_datatype(datatype):
    """
    Check if a datatype value is valid to use.

    :param int datatype: Enum/integer representation of datatype 

    :return bool
    """

    return util.check_datatype(datatype)
