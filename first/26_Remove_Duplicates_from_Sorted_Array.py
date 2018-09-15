#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com




class Solution(object):
    def removeDuplicates_me(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if not length:
            return 0

        index = 0
        earlier = None

        while(index < length):

            if index == 0:
                earlier = nums[index]
                index += 1

            elif nums[index] == earlier:
                for i in range(index+1,length):
                    nums[i-1] = nums[i]
                nums.pop()
                length -= 1

            else:
                earlier = nums[index]
                index += 1


        return len(nums)

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        if not nums:
            return 0

        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
    
        return count        







                         



if __name__ == '__main__':
    solution = Solution() 
    print(solution.removeDuplicates([1,1,2]))