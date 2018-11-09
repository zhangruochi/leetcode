## 思路

- 递归式:
    ```Python
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    ```

- 状态转移方程:
    dp[i] = dp[i-2] + dp[i-1]



- dp 式子
    ```Python
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        
        dp = [1,2]
        for i in range(2,n):
            dp.append(dp[i-2] + dp[i-1])
        return dp[n-1]
    ```