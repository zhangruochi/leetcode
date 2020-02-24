from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        res = 0
        for key, value in Counter(s).items():
            if value % 2 != 0:
                count += 1
            res += value    
                
        if not count:
            return res
        else:
            return res - count + 1
                
                
                