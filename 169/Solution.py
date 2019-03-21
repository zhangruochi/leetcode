"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        from collections import Counter
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common(1)[0][0]

    def majorityElement2(self,nums):
        nums.sort()
        return nums[len(nums)//2]


    def majorityElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        return max(counts.keys(),key = counts.get)



            
if __name__ == '__main__':
    print(Solution().majorityElement2([2,2,1,1,1,2,2]))            

