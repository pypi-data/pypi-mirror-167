"""
Test starting a qwilprobe microservice
"""

import threading
import time

import pytest

from qwilprobe.client.probe import Probe
from qwilprobe.service.api import (
    DATATYPE_INTEGER,
    DATATYPE_REAL,
    DATATYPE_STRING,
    RPC_GET_PROBE_DATA,
    qwilprobe_register_handler,
    qwilprobe_set_probe_info,
    qwilprobe_start,
    qwilprobe_stop,
)
from qwilprobe.shared.constants import (
    KEY_COLINFO,
    KEY_COLINFO_NAME,
    KEY_COLINFO_TYPE,
    KEY_UID,
)

# Test constants
TESTVAL_GOOD_UID = "my-test-service"
TESTVAL_GOOD_COLINFO_NAME = "col1"
TESTVAL_GOOD_COLINFO_TYPE = DATATYPE_INTEGER
TESTVAL_GOOD_COLINFO = [
    {
        KEY_COLINFO_NAME: TESTVAL_GOOD_COLINFO_NAME,
        KEY_COLINFO_TYPE: TESTVAL_GOOD_COLINFO_TYPE,
    },
]

def setup_function():
    """
    Start service in different thread.
    """
    qwilprobe_set_probe_info(TESTVAL_GOOD_UID, TESTVAL_GOOD_COLINFO)
    start_thread = threading.Thread(None, qwilprobe_start)
    start_thread.start()

def teardown_function():
    """
    Always stop the service after a certain amount of time has passed.
    This to prevent pytest from hanging.
    """
    qwilprobe_stop()

def test_connect_get_probe_info_minimal():
    """Test that a client/probe can connect to a service and get its info."""
    probe = Probe()
    probe_info = probe.get_probe_info()
    print(probe_info)

    received_uid = probe_info[KEY_UID]
    received_colinfo = probe_info[KEY_COLINFO]

    assert received_uid == TESTVAL_GOOD_UID
    assert len(received_colinfo) == 1 #  Expect one column for this service
    assert received_colinfo[0][KEY_COLINFO_NAME] == TESTVAL_GOOD_COLINFO_NAME
    assert received_colinfo[0][KEY_COLINFO_TYPE] == TESTVAL_GOOD_COLINFO_TYPE
