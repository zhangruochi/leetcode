class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        dp = [[0] * len(text1) for i in range(len(text2))]
        ## text1 -->j; text2-->i
        
        flag = False
        for i in range(len(text2)):
            if text2[i] == text1[0]:
                flag = True
            if flag:
                dp[i][0] = 1
        
        flag = False
        for j in range(len(text1)):
            if text1[j] == text2[0]:
                flag = True
            if flag:
                dp[0][j] = 1
                
        for i in range(1,len(text2)):
            for j in range(1,len(text1)):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[i][j]