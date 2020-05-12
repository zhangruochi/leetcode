"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

 

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
 

限制：

1 <= n <= 11

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def twoSum(self, n: int) -> List[float]:

        # n  - > 6n

        # dp[n][m] -> n个骰子点数之和m的个数


        dp = [ [0] * (6*n+1) for i in range(n+1) ]

        for _ in range(1, 6 + 1):
            dp[1][_] = 1
        
        for i in range(2, n+1):
            for j in range(i, 6*i+1):
                for cur in range(1, 7):
                    if j - cur <= 0:
                        break
                    dp[i][j] += dp[i-1][j- cur]

        res = []

        print(dp)


        for i in range(n, 6*n+1):
            res.append(dp[-1][i] / (6.0 ** n))
        
        # res.sort()

        return res