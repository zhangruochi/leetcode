"""
704. Binary Search
Easy

526

42

Add to List

Share
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        low, high = 0, len(nums) -1
        
        while low <= high:
            mid = ( high - low ) // 2 + low
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return - 1



def binary_search(nums, target, left, right):

    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if nums[mid] > target:
        return binary_search(nums, target, left, mid-1)
    elif nums[mid] < target:
        return binary_search(nums, target, mid+1, right)
    else:
        return mid
    

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target, 0, len(nums)-1)

