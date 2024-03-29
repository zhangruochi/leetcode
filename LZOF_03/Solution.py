"""
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

限制：
2 <= n <= 100000
"""

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        res = None
        count_0 = 0
        for num in nums:
            res = None
            if nums[abs(num)] < 0:
                res = abs(num)
                break
            elif nums[abs(num)] == 0:
                count_0 += 1
                if count_0 >=2 :
                    res = abs(num)
                    break
            else:
                nums[num] *= -1
        
        return res


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:

        vis = set()
        for n in nums:
            if n in vis:
                break
            vis.add(n)

        return n