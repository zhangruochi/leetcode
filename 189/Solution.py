"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution:

    def moveOne(self,nums):
        last = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            nums[i+1] = nums[i]
        nums[0] = last 

        
        """
        index = len(nums)-2
        while index >= 0:
            nums[index+1] = nums[index]
            index -= 1
        nums[0] = last 
        """     



    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            self.moveOne(nums)
        
        print(nums)    

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = nums[:]
        for i in range(len(nums)):
            nums[(i+k)%len(nums)] = l[i]

        #print(nums)  


    def reverse(self,nums,l,h):
        while l < h:
            nums[l],nums[h] = nums[h],nums[l]
            l += 1
            h -= 1
        

    def rotate3(self,nums,k):
        k = k%len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
        print(nums)
        
              


if __name__ == '__main__':
    Solution().rotate3([-1],2)


    







