class Solution:
    def lastSubstring(self, s: str) -> str:
        
        max_char = max(list(s))
        
        chars = []
        
        res = None
        
        for i, c in enumerate(s):
            if c == max_char:
                if not res:
                    res = s[i:]
                else:
                    if s[i:] >  res:
                        res = s[i:]
                        
        return res
                
        
                