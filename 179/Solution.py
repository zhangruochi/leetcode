"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
"""

class Solution:
    
    def compare(self,num1,num2):
        return True if num1+num2 >= num2+num1 else False

    def merge(self,list1,list2):
        result = []
        p1,p2 = 0,0
        while p1 < len(list1) and p2 < len(list2):
            if self.compare( list1[p1],list2[p2]):
                result.append(list1[p1])
                p1 += 1
            else:
                result.append(list2[p2])
                p2 +=1
        result += list1[p1:]
        result += list2[p2:]
        
        return result
                
    
    def merge_sort(self,nums):
        if len(nums) <= 1:
            return nums

        length = len(nums)
        
        return self.merge(self.merge_sort(nums[:length//2]),self.merge_sort(nums[length//2:]))
        
    
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not any(nums):
            return "0"
        
        nums = list(map(str,nums))
        
        return "".join(self.merge_sort(nums))