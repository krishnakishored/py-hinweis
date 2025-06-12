#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Write your code here
    # Initialize a list of zeros with a size of 100 (for numbers 0-99)
    count = [0] * 100
    # Count occurrences of each number in the input array
    for num in arr:
        count[num] += 1
    # # Create a new list to store the sorted result
    sorted_arr = []
    # # Append each number to the sorted array according to its count
    for i in range(100):
        sorted_arr.extend([i] * count[i])
    return sorted_arr


# def countingSort(arr):
#     # Write your code here
#     # initialize the freq_array

#     max_value = max(arr)
#     min_value = min(arr)

#     ranges = (max_value-min_value+1)
#     freq_array = [0] * 100
#     for num in arr:
#         freq_array[num] += 1
#     sorted_arr = []
#     # # Append each number to the sorted array according to its count
#     # for i in range(100):
#     #     sorted_arr.extend([i] * freq_array[i])
#     # return sorted_arr

#     return freq_array


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    # result = countingSort(arr)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Example input for testing
    result = countingSort(arr)
    print(" ".join(map(str, result)))  # Print the result for testing purposes
