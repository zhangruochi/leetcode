"""
665. Non-decreasing Array
Easy

1512

353

Add to List

Share
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """ 
        non-decreasing detecting
        """
        if len(nums) <= 1:
            return True
    
    
        # increasing
        # 4,2,3  -> 2,2,3
        # 2,4,3  -> 2,3,3
        # 2,4,1  -> 2,4,4
        count = 0
    
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if (i == 1 or nums[i] >= nums[i - 2]): 
                    nums[i-1] = nums[i];
                else:
                    nums[i] = nums[i - 1]
                
                count += 1
                
            if count == 2:
                return False
            
        return True
            
            
            
    
    
                
            
        
        