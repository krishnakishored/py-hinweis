# https://www.hackerrank.com/challenges/np-arrays/problem

import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr, float)
    """
    arr[::] = equivalent to arr[start: stop : step]
    """
    reversed_arr = arr[::-1]
    # return [elem for elem in reversed(result.tolist())]
    return reversed_arr


if __name__ == "__main__":
    arr = input().strip().split(" ")
    result = arrays(arr)
    print(result)
