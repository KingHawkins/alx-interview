#!/usr/bin/python3
"""
Log parsing.
"""
import asyncio
import sys
import shlex


def log():
    """
    Prints the logs every 10 seconds.
    """
    size = {"size": 0}
    statuses = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
    }
    for line in sys.stdin:
        status = shlex.split(line.strip())[-2:-1]
        file_size = shlex.split(line.strip())[-1:]
        if status[0] in statuses.keys():
            statuses[status[0]] += 1
            size["size"] += int(file_size[0])
            print(f"File size: {size['size']}")
            for status in statuses:
                print(f"{status}: {status[0]}")


log()
