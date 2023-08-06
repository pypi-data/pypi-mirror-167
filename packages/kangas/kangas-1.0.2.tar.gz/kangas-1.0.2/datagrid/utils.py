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
import math
import sys
import uuid

import six

RESERVED_NAMES = ["ROW-ID"]


def _in_jupyter_environment():
    # type: () -> bool
    """
    Check to see if code is running in a Jupyter environment,
    including jupyter notebook, lab, or console.
    """
    try:
        import IPython
    except Exception:
        return False

    ipy = IPython.get_ipython()
    if ipy is None or not hasattr(ipy, "kernel"):
        return False
    else:
        return True


def _in_ipython_environment():
    # type: () -> bool
    """
    Check to see if code is running in an IPython environment.
    """
    try:
        import IPython
    except Exception:
        return False

    ipy = IPython.get_ipython()
    if ipy is None:
        return False
    else:
        return True


def _in_colab_environment():
    # type: () -> bool
    """
    Check to see if code is running in Google colab.
    """
    try:
        import IPython
    except Exception:
        return False

    ipy = IPython.get_ipython()
    return "google.colab" in str(ipy)


class ProgressBar:
    """
    A simple ASCII progress bar, showing a box for each item.
    Uses no control characters.
    """

    def __init__(self, sequence, description=None):
        """
        The sequence to iterate over. For best results,
        don't print during the iteration.
        """
        self.sequence = sequence
        if description:
            self.description = "%s " % description
        else:
            self.description = None

    def set_description(self, description):
        self.description = "%s " % description

    def __iter__(self):
        if self.description:
            print(self.description, end="")
        print("[", end="")
        sys.stdout.flush()
        for item in self.sequence:
            print("█", end="")
            sys.stdout.flush()
            yield item
        print("]")


def _input_user(prompt):
    # type: (str) -> str
    """Independent function to apply clean_string to all responses + make mocking easier"""
    return clean_string(six.moves.input(prompt))


def _input_user_yn(prompt):
    # type: (str) -> bool
    while True:
        response = _input_user(prompt).lower()
        if response.startswith("y") or response.startswith("n"):
            break
    return response.startswith("y")


def clean_string(string):
    if string:
        return "".join([char for char in string if char not in ["'", '"', " "]])
    else:
        return ""


def is_nan(value):
    """
    Return True if value is float("NaN")
    """
    return isinstance(value, float) and math.isnan(value)


def is_null(value):
    return value is None or is_nan(value)


def convert_string_to_date(string, datetime_format):
    """
    Attempt to convert a string into a particular type
    of datetime object.

    Args:
        string: (str) the string to attempt to parse into a date
        datetime_format: (str) a datetime format

    Returns:
        A Datetime object if successful, and None otherwise.
    """
    try:
        return datetime.datetime.strptime(string, datetime_format)
    except ValueError:
        return None


def convert_to_value(value, heuristics, datetime_format=None):
    return (
        convert_string_to_value(value, heuristics, datetime_format)
        if isinstance(value, str)
        else value
    )


def convert_string_to_value(value, heuristics, datetime_format=None):
    """
    Takes a string, and returns a value of the appropriate time
    for those situations where you don't have type information
    (like a CSV file).

    Args:
        value: (str) a string from a cell in the spreadsheet
        heuristics: (bool) if True, guess numeric datestamps
        datetime_format: (str) the format of dates

    Examples:
    ```python
    >>> convert_string_to_value("1") # int
    1
    >>> convert_string_to_value("1.1") # float
    1.1
    >>> convert_string_to_value("True") # str
    "True"
    >>> convert_string_to_value("12/1/2001") # str
    "12/1/2001"
    >>> convert_string_to_value("12/1/2001", datetime_format="%m/%d/%Y") # datetime
    datetime.datetime(2001, 12, 1, 0, 0)
    >>> convert_string_to_value(111111111) # datetime, heuristics is True
    datetime.date(1973, 7, 10)
    >>> convert_string_to_value(111111111, heuristics=False) # int
    111111111
    ```
    """
    if value.strip() == "":
        return None

    if datetime_format:
        datetime_value = convert_string_to_date(value, datetime_format)
        if datetime_value:
            return datetime_value

    if value.startswith("-") and len(value) > 0:
        if value[1:].isdigit():
            return int(value)
        elif value.count(".") == 1 and value.replace(".", "").isdigit():
            return float(value)
        else:
            return value
    elif value.isdigit():
        if heuristics:
            if len(value) in [9, 10]:  # could be a datetime
                return datetime.datetime.fromtimestamp(int(value))
            elif len(value) in [13, 14]:  # could be a datetime with ms
                return datetime.datetime.fromtimestamp(int(value) / 1000)
            else:
                return int(value)
        else:
            return int(value)
    elif value.count(".") == 1 and value.replace(".", "").isdigit():
        if heuristics:
            int_part, dec_part = value.split(".")
            if len(int_part) in [9, 10]:  # could be a datetime
                return datetime.datetime.fromtimestamp(float(value))
            elif len(int_part) in [13, 14]:  # could be a datetime with ms
                return datetime.datetime.fromtimestamp(float(value) / 1000)
            else:
                return float(value)
        else:
            return float(value)
    else:
        return value


def sanitize_name(name, delim="-"):
    """
    Remove any unwanted characters and replace with
    the given delimiter.

    Args:
        name: (str) the text to sanitize
        delim: (str) the char to replace unwanted chars

    Returns:
        a sanitized string
    """
    return (
        name.strip()
        .lower()
        .replace(" ", delim)
        .replace("/", delim)
        .replace(":", delim)
        .replace("-", delim)
    )


def make_column_name(num):
    """
    Create an automatic column name, if one isn't given.

    Args:
        num: (int) number of column

    Returns: a string appropriate for a column name
    """
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[num % 26]
    group = (num // 26) + 1
    return char * group


def generate_guid():
    # type: () -> str
    """Generate a GUID"""
    return uuid.uuid4().hex
