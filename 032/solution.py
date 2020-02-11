class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_ans = 0
        dp = [0] * len(s)
        
        for i in range(1,len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    if i >= 2:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                else:
                    if i - dp[i-1] > 0 and s[ i - dp[i -1] - 1] == "(":
                        if i - dp[i -1] - 2 > 0:
                            dp[i] = dp[i-1] + 2 + dp[i - dp[i -1] - 2]
                        else:
                            dp[i] = dp[i-1] + 2
                max_ans = max(max_ans, dp[i])
                
        return max_ans