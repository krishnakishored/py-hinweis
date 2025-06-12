#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isBalanced(s):
    # Write your code here
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in brackets.values():  # If it's an opening bracket
            stack.append(char)
        elif char in brackets.keys():  # If it's a closing bracket
            if not stack or stack[-1] != brackets[char]:
                return "NO"
            stack.pop()  # Pop the last opening bracket if it matches
    return (
        "YES" if not stack else "NO"
    )  # If stack is empty, all brackets are balanced


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + "\n")

    fptr.close()
