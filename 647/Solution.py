"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = len(s)
        
        ## odd palindromic substrings
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
                
                
        
        ## even palindromic substrings
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        return count

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        dp = [[False] * len(s) for i in range(len(s))]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = ((s[i] == s[j]) and ((j - i <= 2) or dp[i+1][j-1]))
                if dp[i][j]:  
                    count += 1

        return count
            
        