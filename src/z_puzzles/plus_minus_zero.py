#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    n_positive, n_negative, n_zero = 0, 0, 0
    for num in arr:
        if num > 0:
            n_positive += 1
        elif num == 0:
            n_zero += 1
        else:
            n_negative += 1
            # {number:.6f}

    result = [
        f"{n_negative / len(arr):.6f}",
        f"{n_positive / len(arr):.6f}",
        f"{n_zero / len(arr):.6f}",
    ]
    print("\n".join(result))

    # print(f"{round(n_negative / len(arr), 6):.6f}")
    # print(f"{round(n_positive / len(arr), 6):.6f}")
    # print(f"{round(n_zero / len(arr), 6):.6f}")


if __name__ == "__main__":
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 1, 0, -1, -1]
    # arr = [1, 1, 0, -1, -1, -1, 0, 0, 0]  # Example input for testing

    plusMinus(arr)
