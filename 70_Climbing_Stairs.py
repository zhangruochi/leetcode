#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

"""


class Solution(object):
    # DP
    def climbStairs_DP(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [1, 2]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n - 1]

    # 递归，暴力穷举
    def climbStairs_RECURSION(self, n):
        return self.climb_Stairs(0, n)

    def climb_Stairs(self, i, n):
        if i > n:
            return 0

        if i == n:
            return 1

        return self.climb_Stairs(i + 1, n) + self.climb_Stairs(i + 2, n)

    # cahce  避免重复计算
    def climbStairs_RECURSION_CAHCE(self, n):
        CAHCE = {}
        return self.climb_Stairs_CACHE(0, n, CAHCE)

    def climb_Stairs_CACHE(self, i, n, CAHCE):
        if i > n:
            return 0

        if i == n:
            return 1

        if i in CAHCE:
            return CAHCE[i]

        CAHCE[i] = self.climb_Stairs_CACHE(i + 1, n, CAHCE) + self.climb_Stairs_CACHE(i + 2, n, CAHCE)

        return CAHCE[i]


if __name__ == '__main__':
    solution = Solution()
    # print(solution.factorial(5))
    # print(solution.perm(1,3))
    print(solution.climbStairs_RECURSION(50))
    print(solution.climbStairs_RECURSION_CAHCE(50))
