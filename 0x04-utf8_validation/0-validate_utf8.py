#!/usr/bin/python3

"""
a method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    num_bytes = 0

    for byte in data:
        # Check if the byte is a continuation bytes
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
                # If the byte doesn't match any UTF-8 encoding pattern
            elif (byte >> 7) != 0:
                return False
        else:
            # Check if the byte is a continuation byte
            if (byte >> 6) != 0b10:
                return False
            # Checking  if there is any  remaining bytes that don't form a complete UTF-8 char
            num_bytes -= 1

    return num_bytes == 0
