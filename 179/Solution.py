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


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        if sum(nums) == 0:
            return "0"


        from functools import cmp_to_key

        # A comparison function is any callable that accept two arguments, compares them, and returns a negative number for less-than, zero for equality, or a positive number for greater-than. A key function is a callable that accepts one argument and returns another value to be used as the sort key.
        def func(a, b):
            return 1 if a + b > b + a else -1

        nums = [str(_) for _ in nums]

        nums.sort(key = cmp_to_key(func), reverse = True)
        
        return "".join(nums)
