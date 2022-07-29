#!/usr/bin/python3
"""A fuction that return list of attributes and methods.
"""


def lookup(obj):
    """ Return the list of available attrributes and methods of an object.
    """
    return dir(obj)
