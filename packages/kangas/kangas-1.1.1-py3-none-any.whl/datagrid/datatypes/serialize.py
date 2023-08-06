# -*- coding: utf-8 -*-
######################################################
#     _____                  _____      _     _      #
#    (____ \       _        |  ___)    (_)   | |     #
#     _   \ \ ____| |_  ____| | ___ ___ _  _ | |     #
#    | |  | )/ _  |  _)/ _  | |(_  / __) |/ || |     #
#    | |__/ ( ( | | | ( ( | | |__| | | | ( (_| |     #
#    |_____/ \_||_|___)\_||_|_____/|_| |_|\____|     #
#                                                    #
#    Copyright (c) 2022 DataGrid Development Team    #
#    All rights reserved                             #
######################################################

import datetime
import json

from .utils import is_nan, is_null


def serialize_identity_function(datagrid, item):
    """
    For FLOAT (mixed float and int) columns.
    """
    if is_nan(item):
        return None

    return item


def serialize_bool_function(datagrid, item):
    if is_null(item):
        return None

    return bool(item)


def serialize_int_function(datagrid, item):
    if is_null(item):
        return None

    return int(item)


def serialize_string_function(datagrid, item):
    if is_null(item):
        return None

    item = str(item)
    return item[: datagrid.MAX_COL_STRING_LENGTH]


def serialize_datetime_function(datagrid, item):
    if is_null(item):
        return None

    if isinstance(item, (int, float)):
        return item
    elif isinstance(item, datetime.datetime):
        return item.timestamp()
    elif isinstance(item, datetime.date):
        return datetime.datetime(item.year, item.month, item.day).timestamp()
    else:
        raise Exception("Can't convert %r to a DATETIME" % item)


def serialize_json_function(datagrid, item):
    if is_null(item):
        return None

    if isinstance(item, (dict,)):
        return json.dumps(item)
    else:
        raise Exception("Can't convert %r to JSON" % item)


def log_and_serialize_function(datagrid, item):
    return item.log_and_serialize(datagrid)


# Mapping from Datatype to allowed types, and serialize
# function:
DATAGRID_TYPES = {
    "BOOLEAN": {
        "types": [bool],
        "serialize": serialize_bool_function,
    },
    "INTEGER": {
        "types": [int],
        "serialize": serialize_int_function,
    },
    "FLOAT": {
        "types": [float],
        "serialize": serialize_identity_function,
    },
    "TEXT": {
        "types": [str],
        "serialize": serialize_string_function,
    },
    "DATETIME": {
        "types": [datetime.date, datetime.datetime],
        "serialize": serialize_datetime_function,
    },
    "JSON": {
        "types": [dict],
        "serialize": serialize_json_function,
    },
}

ASSET_TYPE_MAP = {}


def register_asset_type(name, cls, asset_type):
    if name:
        DATAGRID_TYPES[name] = {
            "types": [cls],
            "serialize": log_and_serialize_function,
        }
    ASSET_TYPE_MAP[asset_type] = cls
