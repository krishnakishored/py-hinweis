#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    # Write your code here
    unique_numbers = set()
    for num in a:
        if num in unique_numbers:
            unique_numbers.remove(num)
        else:
            unique_numbers.add(num)
    return unique_numbers.pop() if unique_numbers else None


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # n = int(input().strip())

    # a = list(map(int, input().rstrip().split()))
    a = [1, 2, 3, 2, 1]  # Example input for testing

    result = lonelyinteger(a)

    # fptr.write(str(result) + "\n")

    # fptr.close()
    print(
        result
    )  # For testing purposes, print the result instead of writing to a file
