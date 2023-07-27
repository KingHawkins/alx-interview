#!/usr/bin/python3
"""
UTF*.8
"""


def validUTF8(data):
    """
    Implementation.
    """
    if all([item <= 255 for item in data]):
        return True
    else:
        return False
