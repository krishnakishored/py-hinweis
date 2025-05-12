class ArraysAndStrings1:
    def __init__(self):
        pass

    def firstUniqChar(self, s):
        """
        Find the first non-repeating character in a string, return its index else '-1'
        :type s: str
        :rtype: int
        example: "leetcode"
        output: 0
        tag: frequency map + order tracking
        """
        from collections import Counter

        print(s, end=" ")
        """1st pass : using Counter"""
        # freq = Counter(s)

        """1st pass: using dictionary"""
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        """Second pass: find first char with frequency 1"""
        for char in s:
            if freq[char] == 1:
                print(s.index(char), char)
                return s.index(char)

        # for i, char in enumerate(s):
        #     if freq[char] == 1:
        #         print(i, char)
        #         return i

        # # using enumerate() & count()
        # for i, char in enumerate(s):
        #     # string.count() is O(n) for each call // O(n^2) for the whole loop - inefficient
        #     if s.count(char) == 1:
        #         print(i, char)
        #         return i

        return -1
        # return -1 if no unique character is found

    def merge(self, intervals):
        """
        Merge overlapping intervals
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        example: [[1,3],[2,6],[8,10],[15,18],[17,20]]
        """
        pass

    def rotate(self, nums, k):
        """
        Rotate the array to the right by k steps
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

    def maxSlidingWindow(self, nums, k):
        """
        Find the maximum in each sliding window of size k
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

    def lengthOfLongestSubstring(self, s):
        """
        Find the length of the longest substring without repeating characters
        :type s: str
        :rtype: int
        """
