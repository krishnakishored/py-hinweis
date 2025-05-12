import pytest
import os
import sys
from io import StringIO

# Add src directory to Python path for imports
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)


from arrays_and_strings.arr_str_1 import ArraysAndStrings1


@pytest.fixture
def solution():
    return ArraysAndStrings1()


def test_first_unique_char(solution):
    print("\nRunning test_first_unique_char:")
    assert solution.firstUniqChar("leetcode") == 0  # 'l' is first unique
    assert solution.firstUniqChar("loveleetcode") == 2  # 'v' is first unique
    assert solution.firstUniqChar("aabb") == -1  # no unique character
    assert solution.firstUniqChar("") == -1  # empty string
    assert solution.firstUniqChar("cc") == -1  # all repeating


def test_merge_intervals(solution):
    print("\nRunning test_merge_intervals...")
    assert solution.mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert solution.mergeIntervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution.mergeIntervals([[1, 3]]) == [[1, 3]]  # single interval
    assert solution.mergeIntervals([]) == []  # empty list
    assert solution.mergeIntervals([[1, 4], [2, 3]]) == [
        [1, 4]
    ]  # completely overlapping


def test_rotate_array(solution):
    print("\nRunning test_rotate_array...")
    # Test case 1: Basic rotation
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    solution.rotateArray(nums1, 3)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4]

    # Test case 2: Rotation with k > array length
    nums2 = [-1, -100, 3, 99]
    solution.rotateArray(nums2, 6)  # equivalent to rotating by 2
    assert nums2 == [3, 99, -1, -100]

    # Test case 3: Empty array
    nums3 = []
    solution.rotateArray(nums3, 0)
    assert nums3 == []

    # Test case 4: Single element
    nums4 = [1]
    solution.rotateArray(nums4, 1)
    assert nums4 == [1]


def test_max_sliding_window(solution):
    print("\nRunning test_max_sliding_window...")
    assert solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        3,
        3,
        5,
        5,
        6,
        7,
    ]
    assert solution.maxSlidingWindow([1], 1) == [1]  # single element
    assert solution.maxSlidingWindow([1, -1], 1) == [1, -1]  # window size 1
    assert solution.maxSlidingWindow([1, 2, 3, 4, 5], 5) == [
        5
    ]  # window size equals array length
    assert solution.maxSlidingWindow([], 0) == []  # empty array


def test_length_of_longest_substring(solution):
    print("\nRunning test_length_of_longest_substring...")
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    assert solution.lengthOfLongestSubstring("bbbbb") == 1  # "b"
    assert solution.lengthOfLongestSubstring("pwwkew") == 3  # "wke"
    assert solution.lengthOfLongestSubstring("") == 0  # empty string
    assert solution.lengthOfLongestSubstring(" ") == 1  # single space
    assert solution.lengthOfLongestSubstring("dvdf") == 3  # "vdf"
