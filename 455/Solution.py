class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0; i = 0; j = 0
        g.sort()
        s.sort()
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i+=1
            j+=1
        
        return res
            
                