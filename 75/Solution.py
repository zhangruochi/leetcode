"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
class Solution:
    def counting_sort(self,colors):
        bucket = [[] for i in range(3)]
        for color in colors:
            bucket[color].append(color)
        
        result = []
        for item in bucket:
            result += item
        return result
    
    
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ## 计数排序
        nums.sort()


from random import randint
class Solution:
    def quick_sort(self,nums,low, high):
        if low >= high:
            return 
        pivot = self.random_partition(nums,low,high)
        self.quick_sort(nums,low,pivot)
        self.quick_sort(nums,pivot+1,high)

    
    def random_partition(self,nums,low,high):
        index = randint(low,high)
        nums[index],nums[high] = nums[high],nums[index]
        i = low
        for j in range(low,high):
            if nums[j] < nums[high]:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        nums[i],nums[high] = nums[high],nums[i]
        return i
 
    
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ## 计数排序
        self.quick_sort(nums,0,len(nums)-1)



def random_partition(self,nums,low,high):
        index = randint(low,high)
        nums[index],nums[high] = nums[high],nums[index]
        i = low
        for j in range(low,high):
            if nums[j] < nums[high]:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        nums[i],nums[high] = nums[high],nums[i]
        return i
 



class Solution:    
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ##self.quick_sort(nums,0,len(nums)-1)
        if len(nums) <= 1:
            return 
        
        point_red,point_blue, index = 0, len(nums)-1,0
        
        index = 0
        while index <= point_blue:

            while nums[point_red] == 0 and point_red < point_blue :
                point_red += 1
            
            while nums[point_blue] == 2 and point_blue > point_red:
                point_blue -= 1
            
            if nums[index] == 2 and index < point_blue:
                nums[index],nums[point_blue] = nums[point_blue],nums[index]
                point_blue -= 1
                
            if nums[index] == 0 and index > point_red:
                nums[index],nums[point_red] = nums[point_red],nums[index]
                point_red += 1
            
            index += 1