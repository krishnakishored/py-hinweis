#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for i in range(n):
        primary_diagonal_sum += arr[i][i]  # Primary diagonal
        # explanation: arr[i][i] accesses the element at row i and column i
        # which is part of the primary diagonal in a square matrix.
        # For example, in a 3x3 matrix, the primary diagonal elements are (0,0), (1,1), and (2,2).
        # The secondary diagonal is accessed by arr[i][n - 1 - i]
        # where n is the size of the matrix, and i iterates from 0 to n-1.
        secondary_diagonal_sum += arr[i][n - 1 - i]  # Secondary diagonal
    return abs(primary_diagonal_sum - secondary_diagonal_sum)
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = []

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Example input for testing

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
