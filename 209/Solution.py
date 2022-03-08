"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

## time complexity O(n) 
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


## time complexity O(nlogn)
class Solution:
    
    ## 查找第一个大于 key 的元素
    def binarySearch(self,nums,key,low,high):
        if high < low:
            return -1
            
        mid = low + ((high-low) >> 1)
        if nums[mid] < key:
            return self.binarySearch(nums,key,mid+1,high)
        else:
            if mid == 0 or nums[mid-1] < key:
                return mid
            else:
                return self.binarySearch(nums,key,low,mid-1)
        
        
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        
        prefix_sums,cum = [0],0
        for num in nums:
            cum += num
            prefix_sums.append(cum)
            
        length = float("inf")
        for i,prefix_sum in enumerate(prefix_sums):
            j = self.binarySearch(prefix_sums,prefix_sum+s,0,len(prefix_sums)-1)
            if j != -1:
                length = min(length,j-i)
        
        return length



class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0

        min_length = float("inf")
        left = sum_ = 0

        for right, val in enumerate(nums):
            sum_ += val
            while sum_ >= target:
                min_length = min(min_length, right - left + 1)
                
                sum_ -= nums[left]
                left += 1

        return min_length
            
