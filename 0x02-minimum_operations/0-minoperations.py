#!/usr/bin/python3
"""
0-minimum operations.
"""


def minOperations(n):
    """
    Implememtation.
    """
    a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            a += b
            n = n / b
        b += 1
    return a
