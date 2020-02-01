"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        
        max_ = len(nums)
        for i in range(max_):
            while nums[i] > 0 and nums[i] <= max_ and nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i],nums[nums[i]-1]
        
        print(nums)
        for index, num in enumerate(nums):
            if index+1 != num:
                return index + 1
        
        return max_ + 1