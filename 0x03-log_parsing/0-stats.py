#!/usr/bin/env python3

"""a script that reads stdin line by line and computes metrics"""

import sys

# Initialize variables to keep track of metrics
total_size = 0
status_codes = {}

try:
    # Read lines from stdin
    for i, line in enumerate(sys.stdin):
        try:
            # Parse input line
            p, status, size = line.split()

            # Convert size to integer
            size = int(size)

            # Update total file size
            total_size += size

            # Update status code count
            if status.isdigit():
                status_codes[int(status)] = status_codes.get(int(status), 0) + 1
        except ValueError:
            # Skip invalid lines
            continue

        # Print statistics after every 10 lines
        if (i + 1) % 10 == 0:
            print("Total file size:", total_size)
            for code in sorted(status_codes):
                print(code, ":", status_codes[code])
            print()

except KeyboardInterrupt:
    # Print statistics when a keyboard interruption occurs
    print("Total file size:", total_size)
    for code in sorted(status_codes):
        print(code, ":", status_codes[code])
