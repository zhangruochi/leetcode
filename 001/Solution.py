"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for index,num in enumerate(nums):
            res = target-num
            if res in table and table[res] != index:
                return [index,table[res]]
            else:
                table[num] = index



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        cache = {}
        res = []

        for i, num in enumerate(nums):
            if target - num in cache:
                res = [cache[target - num], i]
                break
                
            cache[num] = i 
        
        return res