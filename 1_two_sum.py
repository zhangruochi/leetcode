#!/usr/bin/env python3

# -info
# -name   : zhangruochi
# -email  : zrc720@gmail.com


"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    # 最简单但时间复杂度没有通过
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return None

    def twoSum(self, nums, target):
        # 以空间换时间
        table = {}

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in table:
                return table[remain], i
            table[nums[i]] = i

        return None


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3,2,4], 6))
