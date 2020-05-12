"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def sumNums(self, n: int) -> int:
        
        mask = 0xffffffff

        def helper(a,b):
            nonlocal mask 

            a = a & mask
            b = b & mask

            while b:
                tmp = a ^ b
                b = ((a & b) << 1) & mask
                a = tmp
            
            return a

        def sum_(n):
            if n == 1:
                return 1
            return helper(sum_(n-1), n)
        
        return sum_(n)


        
        
