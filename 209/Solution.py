"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s: return 0

        count_ = len(nums)
        sum_,i,j= 0,0,0
        
        while j < len(nums):
            
            while j < len(nums) and sum_ < s:
                sum_ += nums[j]
                j += 1
                
            while sum_ >= s:
                sum_ -= nums[i]
                i += 1

            count_ = min(count_,j-i+1)
               
            
        return count_