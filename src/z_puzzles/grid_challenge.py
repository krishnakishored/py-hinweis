#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    # Sort each row of the grid
    sorted_grid = ["".join(sorted(row)) for row in grid]
    print(sorted_grid)  # For debugging purposes, print the sorted rows
    # Check if the sorted rows are in lexicographical order
    for i in range(1, len(sorted_grid)):
        if sorted_grid[i] < sorted_grid[i - 1]:
            return "NO"
    return "YES"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     n = int(input().strip())

    #     grid = []

    #     for _ in range(n):
    #         grid_item = input()
    #         grid.append(grid_item)

    #     result = gridChallenge(grid)

    #     fptr.write(result + '\n')
    # fptr.close()
    grid = [
        "ebacd",
        "fghij",
        "olmkn",
        "trpqs",
        "xywuv",
    ]  # Example input for testing
    result = gridChallenge(grid)
    print(
        result
    )  # For testing purposes, print the result instead of writing to a file
