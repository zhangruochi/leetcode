"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
Note:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
            
        table,count = {},0
        for prefix_j in prefix_sums:
            count += table.get(prefix_j-k,0)
            
            if not prefix_j in table:
                table[prefix_j] = 1
            else:
                table[prefix_j] += 1
            
        return count
            

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count,cum = 0,0
        prefix_sums = defaultdict(int)
        
        prefix_sums[0] = 1
        
        
        for num in nums:
            cum += num
            count += prefix_sums.get(cum - k, 0)
            prefix_sums[cum] += 1
            
        return count
        