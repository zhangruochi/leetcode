"""
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.
"""

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()

        l,r = 0,len(nums)-1
        min_diff = float("inf")
        res = -1

        while l < r:

            cur_sum = nums[l] + nums[r]
            if cur_sum >= k:
                r -= 1
            elif cur_sum < k:
                l += 1

            diff =  k - cur_sum
            if diff > 0 and diff < min_diff:
                min_diff = diff
                res = cur_sum
        
        return res



        


        
