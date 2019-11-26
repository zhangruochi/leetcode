class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        if not str1 or not str2:
            return ""
        
        
        dp = [[0] * (len(str2)+1) for i in range(len(str1)+1)]
        
        # dp[i][j] -->  i: str1, j: str2
        
        for i in range(1,len(str1)+1):
            for j in range(1,len(str2)+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        l1 = len(str1); l2 = len(str2)
        
        res = []
        
        while l1 or l2:
            if not l1:
                char = str2[l2-1]
                l2 -= 1
            elif not l2:
                char = str1[l1-1]
                l1 -= 1
            elif str1[l1-1] == str2[l2-1]:
                char = str1[l1-1]
                l1 -= 1
                l2 -= 1
            elif dp[l1-1][l2] == dp[l1][l2]:
                char = str1[l1-1]
                l1 -= 1
            elif dp[l1][l2-1] == dp[l1][l2]:
                char = str2[l2-1]
                l2 -= 1
            
            res.append(char)
        
        return "".join(res[::-1])
            
            
                
                
            