"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cum,res = 0, 0
        table = {0: -1}
        
        for i, num in enumerate(nums):
            if num == 0:
                cum -= 1
            if num == 1:
                cum += 1
                
            if cum in table:
                res = max(res, i - table[cum])
            else:
                table[cum] = i
        
        return res
            