#!/usr/bin/env python3

import sys

# Initialize variables

total_size = 0

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

line_count = 0

# Read stdin line by line

for line in sys.stdin:

    try:

        # Parse line

        ip, _, _, _, _, status_code, file_size = line.split()

        # Convert status code and file size to integers

        status_code = int(status_code)

        file_size = int(file_size)

        # Update metrics

        total_size += file_size

        status_codes[status_code] += 1

        line_count += 1

        # Print metrics every 10 lines or on keyboard interrupt

        if line_count % 10 == 0:

            print("Total file size: File size: {}".format(total_size))

            for code in sorted(status_codes.keys()):

                if status_codes[code] > 0:

                    print("{}: {}".format(code, status_codes[code]))

    except ValueError:

        # Skip line if it doesn't match expected format

        continue

# Print final metrics

print("Total file size: File size: {}".format(total_size))

for code in sorted(status_codes.keys()):

    if status_codes[code] > 0:

        print("{}: {}".format(code, status_codes[code]))

