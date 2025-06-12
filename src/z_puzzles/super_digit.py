#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    # Calculate the super digit of a number represented as a string
    def calculate_super_digit(x):
        if len(x) == 1:
            return int(x)
        else:
            digit_sum = sum(int(digit) for digit in x)
            return calculate_super_digit(str(digit_sum))
    # Calculate the initial super digit of n
    initial_super_digit = calculate_super_digit(n)
    # Multiply the initial super digit by k to account for the repetition
    final_super_digit = calculate_super_digit(str(initial_super_digit * k))
    return final_super_digit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
