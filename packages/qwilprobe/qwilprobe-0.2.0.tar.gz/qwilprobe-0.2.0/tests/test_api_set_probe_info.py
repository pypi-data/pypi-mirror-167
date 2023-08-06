"""
Test setting probe info.
"""

import pytest

from qwilprobe.service.api import (
    DATATYPE_INTEGER,
    DATATYPE_REAL,
    DATATYPE_STRING,
    KEY_COLINFO,
    KEY_COLINFO_DESCR,
    KEY_COLINFO_NAME,
    KEY_COLINFO_TYPE,
    KEY_DESCR,
    KEY_UID,
    qwilprobe_set_probe_info,
)

good_column_info = [
                    {
                        KEY_COLINFO_NAME: "col1",
                        KEY_COLINFO_TYPE: DATATYPE_INTEGER,
                    },
                    {
                        KEY_COLINFO_NAME: "column 2",
                        KEY_COLINFO_TYPE: DATATYPE_REAL,
                        KEY_COLINFO_DESCR: ""
                    },
                    {
                        KEY_COLINFO_NAME: "3-column",
                        KEY_COLINFO_TYPE: DATATYPE_STRING,
                        KEY_COLINFO_DESCR: "A column for string data."
                    }
                   ]


def test_set_probe_info_basic():
    """Test setting minimal probe info."""
    qwilprobe_set_probe_info("dummy_uid", good_column_info)


def test_set_probe_info_basic_with_descr():
    """Test setting some basic probe info plus a description."""
    qwilprobe_set_probe_info("dummy_uid",
                             good_column_info,
                             "Service description.")


def test_set_probe_info_basic_with_descr_empty():
    """Test setting some basic probe info plus an empty description."""
    qwilprobe_set_probe_info("dummy_uid",
                             good_column_info,
                             "")


def test_set_probe_info_basic_with_descr_none():
    """Test setting some basic probe info plus a None-type description."""
    qwilprobe_set_probe_info("dummy_uid",
                             good_column_info,
                             None)


def test_set_probe_info_bad_uid_empty():
    """Test that the proper error is raised when uid is the empty string."""
    with pytest.raises(ValueError):
        qwilprobe_set_probe_info("", good_column_info)


def test_set_probe_info_bad_uid_empty():
    """Test that the proper error is raised when uid is None."""
    with pytest.raises(ValueError):
        qwilprobe_set_probe_info(None, good_column_info)


def test_set_probe_info_bad_uid_type():
    """Test that the proper error is raised when uid is a bad type."""
    with pytest.raises(ValueError):
        qwilprobe_set_probe_info(1234, good_column_info)


def test_set_probe_info_bad_uid_type2():
    """Test that the proper error is raised when uid is another bad type."""
    with pytest.raises(ValueError):
        qwilprobe_set_probe_info({"bad": False}, good_column_info)


def test_set_probe_info_bad_column_info_none():
    """Test that the proper exception is raised when column info is None."""
    with pytest.raises(ValueError):
        qwilprobe_set_probe_info("dummy_uid", None)


def test_set_probe_info_bad_column_info_empty():
    """Test that the proper exception is raised when column info is empty."""
    with pytest.raises(ValueError):
        qwilprobe_set_probe_info("dummy_uid", [])


def test_set_probe_info_bad_column_info_emptydicts():
    """Test that the proper exception is raised when columns are empty."""
    with pytest.raises(ValueError):
        qwilprobe_set_probe_info("dummy_uid", [{},{}])


def test_set_probe_info_bad_column_info_type():
    """Test that the proper exception is raised for wrong column info type."""
    with pytest.raises(ValueError):
        bad_type = ("hej", 7)
        qwilprobe_set_probe_info("dummy_uid", bad_type)


def test_set_probe_info_bad_column_colname():
    """Test that the proper exception is raised when a column name is bad."""
    with pytest.raises(ValueError):
        bad_colname = [{KEY_COLINFO_NAME: {}, KEY_COLINFO_TYPE: DATATYPE_REAL}]
        qwilprobe_set_probe_info("dummy_uid", bad_colname)


def test_set_probe_info_bad_column_info_coltype():
    """Test that the proper exception is raised when column type is bad."""
    with pytest.raises(ValueError):
        bad_coltype = [{KEY_COLINFO_NAME: "c", KEY_COLINFO_TYPE: -1}]
        qwilprobe_set_probe_info("dummy_uid", bad_coltype)


def test_set_probe_info_bad_column_info_missing_name():
    """Test that the proper exception is raised when column name is missing."""
    with pytest.raises(ValueError):
        bad_coltype = [{KEY_COLINFO_TYPE: DATATYPE_REAL}]
        qwilprobe_set_probe_info("dummy_uid", bad_coltype)


def test_set_probe_info_bad_column_info_missing_type():
    """Test that the proper exception is raised when column type is missing."""
    with pytest.raises(ValueError):
        bad_coltype = [{KEY_COLINFO_NAME: "c"}]
        qwilprobe_set_probe_info("dummy_uid", bad_coltype)


def test_set_probe_info_bad_descr_1():
    """Test that an exception is raised when service description is bad 1."""
    with pytest.raises(ValueError):
        qwilprobe_set_probe_info("dummy_uid", good_column_info, 7)


def test_set_probe_info_bad_descr_2():
    """Test that an exception is raised when service description is bad 2."""
    with pytest.raises(ValueError):
        qwilprobe_set_probe_info("dummy_uid", good_column_info, str)


def test_set_probe_info_bad_descr_3():
    """Test that an exception is raised when service description is bad 3."""
    with pytest.raises(ValueError):
        qwilprobe_set_probe_info("dummy_uid", good_column_info, ("hello",))
