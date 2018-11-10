"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high = 0,len(nums)-1
        if len(nums) == 1:
            return nums[-1]
        if nums[-1] > nums[0]:
            return nums[0]
        
        while low <= high:
            mid = low + ((high-low)>>1)

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[mid] >= nums[low]:
                low = mid + 1
            elif nums[mid] <= nums[high]:
                high = mid - 1
                   
        return -1