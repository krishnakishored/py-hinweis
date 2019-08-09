# https://www.python-course.eu/numpy_create_arrays.php

import numpy as np

def test_create_arrays():
    a = np.arange(1, 10)
    print(a)
    x = range(1, 10)
    print(x)    # x is an iterator   # range(1, 10)
    print(list(x)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # further arange examples:
    x = np.arange(10.4) 
    print(x) # [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
    x = np.arange(0.5, 10.4, 0.8)
    print(x)  # [ 0.5  1.3  2.1  2.9  3.7  4.5  5.3  6.1  6.9  7.7  8.5  9.3 10.1]
    x = np.arange(0.5, 10.4, 0.8, int)
    print(x)


if __name__ == "__main__":
    test_create_arrays()