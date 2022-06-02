"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        def helper(l, r):
            if l > r:
                return l

            mid = (l + r) // 2

            if nums[mid] > target:
                return helper(l, mid-1)
            else:
                if nums[mid] == target:
                    return mid
                    
                elif (mid < len(nums)-2 and nums[mid] < target and nums[mid+1] > target):
                    return mid + 1
                else:
                    return helper(mid+1, r)
        
        return helper(0, len(nums)-1)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 

        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        if i == 0:
            nums[:] = sorted(nums)
        else:
            r = len(nums) - 1
            while nums[r] <= nums[i-1]:
                r -= 1

            nums[i-1], nums[r] = nums[r], nums[i-1]
            nums[i:] = sorted(nums[i:])

                