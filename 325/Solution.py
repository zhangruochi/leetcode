"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""

class Solution:
    

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        table,cum,length = {},0,0
        for j,num in enumerate(nums):
            cum += num
            if cum == k:
                length = j+1
            else:
                if cum-k in table:
                    length = max(length,j - table.get(cum-k))
        
            if not cum in table:
                table[cum] = j
                
        return length


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        indices = {}   
        max_dis = 0
        prefix_sums, cum = [0],0
        
        for num in nums:
            cum += num
            prefix_sums.append(cum)
              
        # prfix_sums[j] - prefix_sums[i] = s  ---> prfix_sums[j]  -  s = prefix_sums[i]
        for i,s in enumerate(prefix_sums):

            if s not in indices:
                indices[s] = i
            t = prefix_sums[i] - k
            if t in indices:
                max_dis = max(max_dis, i - indices[t])
        
        return max_dis



        