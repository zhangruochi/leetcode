class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        def check(s):
            return True if s[::-1] == s else False
        
        tmp = ""
        i = len(s)-1
        res = s
        
        while i >= 0:
            
            if check(res):
                return res
            
            
            tmp += s[i]
            i-=1
            res = tmp + s
            
        return ""
        