import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Initialize with first element
    total = min_val = max_val = arr[0]
    
    # Start loop from second element
    for num in arr[1:]:
        total += num
        min_val = min(min_val, num)
        max_val = max(max_val, num)
    
    # Min sum is total minus max value
    # Max sum is total minus min value
    print(f"{total - max_val} {total - min_val}")

if __name__ == "__main__":
    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]  # Example input for testing

    miniMaxSum(arr)
