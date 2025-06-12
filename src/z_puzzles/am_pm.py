#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):

    time_parts = s.split(":")
    hours, minutes, seconds = (
        int(time_parts[0]),
        time_parts[1],
        time_parts[2][:2],
    )
    period = time_parts[2][2:]
    if period == "AM":
        if hours == 12:
            hours = 0
    elif period == "PM":
        if hours != 12:
            hours += 12
    result = f"{hours:02d}:{minutes}:{seconds}"
    # print(result)
    return result

    # # Write your code here
    # # Split the time into components
    # time_parts = s[:-2].split(':')
    # hour = int(time_parts[0])
    # minute = time_parts[1]
    # second = time_parts[2]
    # period = s[-2:]
    # # Convert hour based on AM/PM
    # if period == 'AM':
    #     if hour == 12:
    #         hour = 0  # Midnight case
    # else:  # PM case
    #     if hour != 12:
    #         hour += 12  # Convert to 24-hour format
    # # Format the hour to two digits
    # hour_24 = f"{hour:02}"
    # # Return the formatted time
    # return f"{hour_24}:{minute}:{second}"


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # s = input()
    s = "12:01:00AM"  # Example input for testing

    result = timeConversion(s)

    print(result)

    # fptr.write(result + "\n")

    # fptr.close()
