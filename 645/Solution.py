"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Note:

The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        num_map = {key: 0 for key in range(1, len(nums) + 1)}
        for num in nums:
            num_map[num] += 1
        return [num for num in num_map if num_map[num] == 2] + [num for num in num_map if num_map[num] == 0]

    def findErrorNums2(self,nums):
        res = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
                    

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)

        return res                
                    


if __name__ == '__main__':
    print(Solution().findErrorNums2([3,3,1]))
