"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        cur_max = nums[0]
        cur_min = nums[0]
        res = nums[0]
        
        for num in nums[1:]:
            ## Must contain current value so we will get a configuous subarrays
            temp = cur_max
            cur_max = max([num, cur_max * num, cur_min * num])
            cur_min = min([num, temp * num, cur_min * num])
            res = max(cur_max, res)
            
        return res
            