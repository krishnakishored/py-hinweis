class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of both arrays
        a = m - 1  # Pointer for nums1's valid elements
        b = n - 1  # Pointer for nums2
        i = m + n - 1  # Pointer for placement in nums1

        # Merge in reverse order to avoid overwriting elements in nums1
        while a >= 0 and b >= 0:
            # Place the larger of nums1[a] or nums2[b] at the end of nums1
            if nums1[a] > nums2[b]:
                nums1[i] = nums1[a]
                a -= 1
            else:
                nums1[i] = nums2[b]
                b -= 1
            i -= 1

        # If any elements remain in nums2, copy them
        while b >= 0:
            nums1[i] = nums2[b]
            b -= 1
            i -= 1


# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
# 
