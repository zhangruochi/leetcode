"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_lens = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    max_lens[i] = max(max_lens[j]+1, max_lens[i])
        
        return max(max_lens)


class Solution:
    
    def binarySearch(self,maxLens,num):
        low = 0; high = len(maxLens)-1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if num > maxLens[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLens = []
        for num in nums:
            pos = self.binarySearch(maxLens,num)
            if pos < len(maxLens):   
                maxLens[pos] = num
            else:
                maxLens.append(num)
        return len(maxLens)
            