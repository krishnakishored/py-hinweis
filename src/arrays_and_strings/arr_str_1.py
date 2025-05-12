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

    def mergeIntervals(self, intervals):
        """
        Merge overlapping intervals
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        example: [[1,3],[2,6],[8,10],[15,18],[17,20]]
        """
        if not intervals:
            return []
        # Sort the intervals based on the start value
        # sort() is in-place and return None - (use sorted() to return a new list)
        intervals.sort(key=lambda x: x[0])
        merged = [
            intervals[0]
        ]  # Initialize a result list with the first interval
        for current in intervals[1:]:
            last = merged[-1]
            # If the current interval overlaps with the last one in the result, merge them
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                # Else, append the current interval to the result
                merged.append(current)
        print(intervals, "merged:", merged)
        return merged

    def rotateArray(self, nums, k):
        """
        Rotate the array to the right(inplace) by k steps
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        example: [1,2,3,4,5,6,7], k=3
        output: [5,6,7,1,2,3,4]
        """

        n = len(nums)
        if n == 0:
            return

        k %= n  # Handle k > n

        nums.reverse()  # # Reverse the entire array(in-place)
        nums[:k] = reversed(nums[:k])  # Reverse the first k elements
        nums[k:] = reversed(nums[k:])  # Reverse the remaining n-k elements
        print(nums, k)

        """with own reverse function"""
        # def reverse(arr, start, end):
        #     while start < end:
        #         arr[start], arr[end] = arr[end], arr[start]
        #         start += 1
        #         end -= 1

        # reverse(nums, 0, n - 1)  # Reverse the entire array
        # reverse(nums, 0, k - 1)  # Reverse the first k elements
        # reverse(nums, k, n - 1)  # Reverse the remaining n-k elements

        """with extra space"""
        # rotated = nums[-k:] + nums[:-k]  # Create a new rotated array
        # for i in range(n):
        #     nums[i] = rotated[i]

        """brute force - shift one by one - inefficient"""
        # for _ in range(k):
        #     # Store the last element
        #     last = nums[-1]

        #     # Shift all elements one position to the right
        #     for i in range(n - 1, 0, -1):
        #         nums[i] = nums[i - 1]

        #     # Place the last element at the first position
        #     nums[0] = last

    def maxSlidingWindow(self, nums, window_size):
        """
        Find the maximum element in each sliding window of size k using a deque data structure.
        The deque maintains indices of potential maximum values in decreasing order.

        :type nums: List[int]
        :type window_size: int
        :rtype: List[int]

        Time Complexity: O(n) where n is length of nums
        Space Complexity: O(k) where k is window_size

        Example:
        Input: nums = [1,3,-1,-3,5,3,6,7], window_size = 3
        Output: [3,3,5,5,6,7]
        Explanation:
            Window position                Deque indices     Max
            ---------------               -------------     -----
            [1  3  -1] -3  5  3  6  7    [1]               3     # deque stores index of 3
            1 [3  -1  -3] 5  3  6  7     [1,2]             3     # deque stores indices of 3,-1
            1  3 [-1  -3  5] 3  6  7     [4]               5     # deque stores index of 5
            1  3  -1 [-3  5  3] 6  7     [4]               5     # deque stores index of 5
            1  3  -1  -3 [5  3  6] 7     [6]               6     # deque stores index of 6
            1  3  -1  -3  5 [3  6  7]    [6,7]             7     # deque stores indices of 6,7

        Note: The deque maintains indices in decreasing order of their corresponding values.
        This allows us to efficiently track the maximum element in each window.
        tag: sliding window + deque
        """
        from collections import deque

        # Handle edge cases
        if not nums or window_size == 0:
            return []

        # Initialize result list to store maximum values
        max_values = []
        # Initialize deque to store indices of potential maximum values
        window_indices = deque()

        for current_idx in range(len(nums)):
            # Step 1: Remove indices that are outside the current window
            # If the leftmost index is outside the window (i - k + 1), remove it
            if (
                window_indices
                and window_indices[0] < current_idx - window_size + 1
            ):
                window_indices.popleft()

            # Step 2: Remove all elements smaller than the current element from the back
            # This maintains decreasing order in the deque
            while (
                window_indices and nums[window_indices[-1]] < nums[current_idx]
            ):
                window_indices.pop()

            # Step 3: Add current index to the deque
            window_indices.append(current_idx)

            # Step 4: Add maximum element to result when we have a complete window
            # First window is complete when we reach index k-1
            if current_idx >= window_size - 1:
                # The front of deque always contains the maximum for current window
                max_values.append(nums[window_indices[0]])

        print(f"Input array: {nums}, Window size: {window_size}")
        print(f"Maximum values in each window: {max_values}")
        return max_values

    def lengthOfLongestSubstring(self, s):
        """
        Find the length of the longest substring without repeating characters using sliding window.

        :type s: str
        :rtype: int

        Example:
        Input: "abcabcbb"
        Output: 3
        Explanation: The longest substring is "abc" with length 3

        Time Complexity: O(n) where n is length of string
        Space Complexity: O(min(m,n)) where m is size of character set

        Approach:
        - Use sliding window with two pointers (left, right)
        - Use set to track characters in current window
        - Expand window to right until duplicate found
        - Contract window from left until duplicate removed

        tag: sliding window
        """
        # Set to store characters in current window
        char_set = set()
        # Left pointer of sliding window
        left = 0
        # Track maximum length seen so far
        max_length = 0

        # Right pointer iterates through string
        for right in range(len(s)):
            # If current char is already in window,
            # contract window from left until duplicate is removed
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove leftmost char
                left += 1  # Contract window

            # Add current char to window
            char_set.add(s[right])

            # Update max_length with current window size
            # Window size is (right - left + 1)
            max_length = max(max_length, right - left + 1)

        # Debug print
        print(
            f"Input string: {s}, Length of longest substring without repeating characters: {max_length}"
        )
        return max_length
