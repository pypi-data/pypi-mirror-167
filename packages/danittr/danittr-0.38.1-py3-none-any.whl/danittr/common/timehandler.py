"""Facility for time related tools."""

from datetime import datetime


def get_isostring_datetime():
    """Return a iso formated today datetime, including time.

    get_isostring_datetime() -> str

    For instance:
    get_isostring_datetime -> '2018-04-02 14:22:36'

    >>> date_regex = '[0-9]{4}-[01][0-9]-[0-3][0-9]'
    >>> time_regex = '[0-2][0-9]:[0-5][0-9]:[0-5][0-9]'
    >>> full_regex = "{} {}".format(date_regex, time_regex)
    >>> isostr = get_isostring_datetime()
    >>> from re import fullmatch
    >>> bool(fullmatch(full_regex, isostr))
    True
    """
    return datetime.now().strftime("%Y-%m-%d %T")
