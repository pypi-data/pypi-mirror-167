from six import string_types, binary_type

import locale

try:
    locale.setlocale(locale.LC_ALL, '')
    CHARSET = locale.getlocale(locale.LC_CTYPE)[1]
except locale.Error:
    CHARSET = None
if CHARSET is None:
    CHARSET = 'ascii'


def is_iterable(obj):
    """ Method that verifies if an object is iterable and not a string, example:

        >>>types.is_iterable(1)
        False
        >>> types.is_iterable([1, 2, 3])
        True

    :param obj: Any object that will be tested if is iterable
    :return: True or False if the object can be iterated
    """
    return hasattr(obj, '__iter__') and not isinstance(obj, string_types + (binary_type,))


def decode(string, errors='replace'):
    if isinstance(string, binary_type) and not isinstance(string, string_types):
        return string.decode(encoding=CHARSET, errors=errors)
    return string


def encode(string, errors='replace'):
    if isinstance(string, string_types) and not isinstance(string, binary_type):
        return string.encode(encoding=CHARSET, errors=errors)
    return string
