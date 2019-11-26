class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            same = 0
        else:
            dp = [[0] * len(word1) for i in range(len(word2))]
            ## text1 -->j; text2-->i

            flag = False
            for i in range(len(word2)):
                if word2[i] == word1[0]:
                    flag = True
                if flag:
                    dp[i][0] = 1

            flag = False
            for j in range(len(word1)):
                if word1[j] == word2[0]:
                    flag = True
                if flag:
                    dp[0][j] = 1

            for i in range(1,len(word2)):
                for j in range(1,len(word1)):
                    if word2[i] == word1[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])

            same = dp[i][j]
        
        return len(word1) + len(word2) - same*2