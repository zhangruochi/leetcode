class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        
        # A --> j
        # B --> i
        
        if not A or not B:
            return 0
        
        
        dp = [[0]*len(A) for i in range(len(B))]
        res = 0
        
        for j in range(len(A)):
            if A[j] == B[0]:
                dp[0][j] = 1
                res = max(res,dp[0][j])
                
        for i in range(len(B)):
            if B[i] == A[0]:
                dp[i][0] = 1
                res = max(res,dp[i][0])
    
        
        for i in range(1,len(A)):
            for j in range(1,len(B)):
                if B[i] == A[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res,dp[i][j])
            
        return res
                    