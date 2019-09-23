"""python
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        def helper(n,m):
            if n == 0:
                return [""]
            if n == 1:
                return ["0","1","8"]
            
            res = []
            for num in helper(n-2,m):
                if n != m:
                    res.append("0" + num + "0")
                res.append("1" + num + "1")
                res.append("8" + num + "8")
                res.append("6" + num + "9")
                res.append("9" + num + "6")
            
            return res
        
        return helper(n,n)
                            