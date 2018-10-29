"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count,pointer = 0,0
        
        for num in nums:
            if num == 0:
                count += 1
                continue
            nums[pointer] = num
            pointer += 1
        nums[pointer:] = [0] * (len(nums)-pointer)