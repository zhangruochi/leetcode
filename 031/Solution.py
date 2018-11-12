"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


from random import randint

class Solution:
    
    def partition(self,nums,left,right):
        pivot = random.randint(left,right)
        nums[pivot],nums[right] = nums[right],nums[pivot]
        
        i = left
        for j in range(left,right):
            if nums[j] < nums[right]:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        nums[right],nums[i] = nums[i],nums[right]
        return i
    
    
    def quick_sort(self,nums,left,right):
        if left >= right:
            return 
        pivot = self.partition(nums,left,right)
        self.quick_sort(nums,left,pivot-1)
        self.quick_sort(nums,pivot+1,right)

    
    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        flag = False
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                flag = True
                break
        
        if not flag:
            nums.reverse()
            return 
        
        
        min_ = float("inf")
        min_index = i
        for j in range(len(nums)-1,i,-1):
            if nums[j] > nums[i] and nums[j] < min_:
                min_ = nums[j]
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
        
        self.quick_sort(nums,i+1,len(nums)-1)
        
 