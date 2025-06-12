#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    # result = []
    # for char in s:
    #     if char.isalpha():
    #         # Shift character within the bounds of a-z or A-Z
    #         shift = (
    #             (ord(char) - ord("a") + k) % 26 + ord("a")
    #             if char.islower()
    #             else (ord(char) - ord("A") + k) % 26 + ord("A")
    #         )
    #         result.append(chr(shift))
    #     else:
    #         result.append(char)
    # return "".join(result)

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k = k % 26  # Normalize k to avoid unnecessary full rotations
    result = []
    for char in s:
        if char in lowercase:
            # Find the new character by shifting within lowercase letters
            new_char = lowercase[(lowercase.index(char) + k) % 26]
            result.append(new_char)
        elif char in uppercase:
            # Find the new character by shifting within uppercase letters
            new_char = uppercase[(uppercase.index(char) + k) % 26]
            result.append(new_char)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # n = int(input().strip())

    # s = input()

    # k = int(input().strip())
    s = "middle-Outz"  # Example input for testing
    k = 3  # Example shift value for testing
    result = caesarCipher(s, k)
    print(
        result
    )  # For testing purposes, print the result instead of writing to a file

    # fptr.write(result + "\n")

    # fptr.close()
