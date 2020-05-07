"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums <= 10000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import partial

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        
        def get_bit(num, idx = None):
            if idx:
                return "{:0>32b}".format(num)[idx]
            else:
                return "{:0>32b}".format(num)


        res = []


        xor_ = 0
        for num in nums:
            xor_  ^= num

        # find the first bit which is equal to 1
        idx = -1
        for i, b in enumerate(get_bit(xor_)):
            if b == "1":
                idx = i
                break
        
        partial_get_bit = partial(get_bit, idx = idx)
    
        # split tow subset according to idx
        xor_ = 0
        for num in nums:
            if partial_get_bit(num) == "1":
                xor_ ^= num
        
        res.append(xor_)

        xor_ = 0
        for num in nums:
            if partial_get_bit(num) == "0":
                xor_ ^= num
        
        res.append(xor_)

        return res

            
from functools import reduce

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        
        res = reduce(lambda x,y: x^y, nums)
        idx = 1
        while idx & res == 0:
            idx = idx << 1

        a,b = 0, 0
        for num in nums:
            if num & idx == 0:
                a ^= num
            else:
                b ^= num
        
        return [a,b]
        

