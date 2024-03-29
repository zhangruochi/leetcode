"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) < 3 or nums[-1] < 0 or nums[0] > 1: return []
        
        result = []
        for index,num in enumerate(nums):
            if num > 0:
                break
            if index > 0 and nums[index-1] == nums[index]:
                continue
            target = -num
            i,j = index+1,len(nums)-1
            while i<j:
                if nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    result.append([num,nums[i],nums[j]])
                    while i<j and nums[i+1] == nums[i]:
                        i += 1
                    while i<j and nums[j-1] == nums[j]:
                        j -= 1
                    i+= 1; j-= 1
        return result


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        res = set()
        i = 0

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            two_sum = 0 - nums[i]

            j = i+1
            k = len(nums)-1

            while j < k:
                
                if nums[j] + nums[k] == two_sum:
                    res.add((nums[i], nums[j], nums[k]))
                    j+=1
                elif nums[j] + nums[k] > two_sum:
                    k -= 1
                else:
                    j += 1

        return [list(_) for _ in res]

                
                


    