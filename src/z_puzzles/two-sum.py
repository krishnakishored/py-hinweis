# 1. Two Sum Problem
# Description: Given a list of integers and a target sum, find two distinct indices such that their values add up to the target.

# Skills Tested: Loops, conditionals, list operations, and dictionary/hash map usage.

# Example:
# Input: [2,[5][7][9], target: 11
# Output: [2] (since 2 + 9 = 11).


def two_sum(nums, target):
    result_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in result_dict:
            return [result_dict[complement], i]
        result_dict[num] = i

    # num_dict = {}
    # for i, num in enumerate(nums):
    #     complement = target - num
    #     if complement in num_dict:
    #         return [num_dict[complement], i]
    #     num_dict[num] = i
    # return None


if __name__ == "__main__":
    nums = [2, 5, 7, 1, 8, 6, 9]
    target = 11
    result = two_sum(nums, target)
    print(result)  # Expected output: [2, 3] since nums[2] + nums[3] = 11
