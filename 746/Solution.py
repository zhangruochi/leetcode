class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0],cost[1])
        
        cost.append(0)
        dp = [-1] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-2],dp[i-1])
        
        return dp[-1]