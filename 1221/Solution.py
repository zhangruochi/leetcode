class Solution:
    def balancedStringSplit(self, s: str) -> int:
        v = 0 
        res = 0
        for c in s:
            if c == "L":
                v += 1
            else:
                v -= 1
            
            if v == 0:
                res += 1
        return res