"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        max_ = 1
        ans = s[0]
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                l,h,count = i-1,i,0
                while l>=0 and h< len(s) and s[l] == s[h]:
                    count += 2
                    l-=1;h+=1
                if count > max_:
                    max_ = count
                    ans = s[l+1:h]
                    
            
            if i+1 < len(s) and s[i-1] == s[i+1]:
                l,h,count = i-1,i+1,1
                while l>=0 and h< len(s) and s[l] == s[h]:
                    count += 2
                    l-=1;h+=1
                if count > max_:
                    max_ = count
                    ans = s[l+1:h]
                    
        return ans


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_ = 0
        ans = ""
        dp = [[False]*len(s) for i in range(len(s))]
        for j in range(len(s)):
            for i in range(0,j+1):
                dp[i][j] = (s[i] == s[j]) and (j-i <= 2 or dp[i+1][j-1])
                if dp[i][j] and (j-i+1) > max_:
                    max_ = j-i+1
                    ans = s[i:j+1]
        return ans


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        
        res = s[0]
        for i in range(len(s)):
            l = i-1
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            
            if r - l - 1 > len(res):
                res = s[l+1:r]
            
            l = i
            r = i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1; r+= 1
                
            if r - l - 1 > len(res):
                res = s[l+1:r]
            
        
        return res


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s

        # dp[i][j] 表示从j开始到i结束的字符串是否为回文串
        dp = [[False] * len(s) for _ in range(len(s))]

        # 长度为1的子串
        for i in range(len(s)):
            dp[i][i] = True

        # dp[i-1][j+1] = 1 if dp[i][j] and s[i-1] == s[j+1]

        max_len = 1
        start = end = 0

        for i in range(1, len(s)):
            for j in range(i):
                if i-j <= 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        cur_len = i-j+1
                else:
                    if dp[i-1][j+1] and s[i] == s[j]:
                        dp[i][j] = True
                        cur_len = i-j+1
                
                if dp[i][j]:
                    if cur_len > max_len:
                        max_len = cur_len
                        start = j
        
        return s[start:start+max_len]