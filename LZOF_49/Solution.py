"""
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。
注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from heapq import *

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        queue = [1]
        visited = set([1])
        count = 0
        while count < n:
            cur = heappop(queue)
            count += 1
            for num in (2,3,5):
                cur_num  = cur * num
                if cur * num not in visited:
                    visited.add(cur_num)
                    heappush(queue, cur_num)
        return cur
        
        
from heapq import *

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        dp = [1] * n
        a,b,c = 0,0,0

        for i in range(1,n):
            a_,b_,c_ = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(a_,min(b_,c_))

            if dp[i] == a_: a+= 1
            if dp[i] == b_: b+= 1
            if dp[i] == c_: c+= 1
        
        return dp[-1]

        
        



