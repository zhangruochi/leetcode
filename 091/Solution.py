class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":return 0
        if len(s) == 1: return 1
        
        if s[1] == "0":
            if s[0:2] > "26":
                dp = [1,0]
            else:
                dp = [1,1]
        else:
            if s[0:2] > "26":
                dp = [1,1]
            else:
                dp = [1,2]
                            
        
        for i in range(2,len(s)):
            if s[i-1] == "0" and s[i] == "0":
                return 0
            elif s[i-1] != "0" and s[i] == "0":
                if s[i-1:i+1] <= "26":
                    dp.append(dp[i-2])
                else:
                    return 0
            elif s[i-1] == "0" and s[i] != "0":
                dp.append(dp[i-1])
            else:
                if s[i-1:i+1] <= "26":
                    dp.append(dp[i-2] + dp[i-1])
                else:
                    dp.append(dp[i-1])
            
            
        return dp[len(s)-1]
        
                
            
        

if __name__ == '__main__':
    solution = Solution()
    s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
    print(solution.numDecodings(s))
