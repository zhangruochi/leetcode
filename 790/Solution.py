class Solution:
    def numTilings(self, N: int) -> int:
        
        if N < 3:
            return N
        
        dp = [[-1] * 3 for i in range(N)]
        
        dp[0][0] = 1
        dp[0][1] = 1
        dp[0][2] = 1
        
        dp[1][0] = 2
        dp[1][1] = 2
        dp[1][2] = 2
        
        
        for i in range(2,N):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-2][1] + dp[i-2][2]
            dp[i][1] = dp[i-1][0] + dp[i-1][2]
            dp[i][2] = dp[i-1][0] + dp[i-1][1]
            
        return dp[-1][0] % (10**9+7)
        
    
        