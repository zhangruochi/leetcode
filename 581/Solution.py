"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:

Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        i,j = 0,len(nums)-1
        
        while i <= len(nums)-1:
            if sorted_nums[i] != nums[i]:
                break
            i+= 1
        
        while j >= 0:
            if sorted_nums[j] != nums[j]:
                break
            j-=1
        
        return j - i + 1 if  j > i else 0

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start = -1; end = -2
        mx = nums[0]
        mn = nums[n-1]
        
        for i in range(n):
            mx = max(nums[i],mx)
            mn = min(nums[n-i-1],mn)
            
            if mx > nums[i]:
                end = i
            if mn < nums[n-1-i]:
                start = n - 1 - i 
                
        return end - start + 1
            
                
            
        