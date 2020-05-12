"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def isStraight(self, nums: List[int]) -> bool:

        count = 0
        non_zeros = []
        for num in nums:
            if num == 0:
                count += 1
            else:
                non_zeros.append(num)
        
        non_zeros.sort()

        for i in range(1, len(non_zeros)):
            if non_zeros[i] - non_zeros[i-1] == 0:
                return False
                
            count -= (non_zeros[i] - non_zeros[i-1] - 1)
            if count < 0:
                return False
            
        return True