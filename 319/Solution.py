from collections import Counter
class Solution:
    def bulbSwitch(self, n: int) -> int:
#         if not n: return 0
        
#         init = int("1"*n,2)
#         for i in range(2,n+1):
#             base = "0"*(i-1) + "1"
#             mask = (base * (n//i + 1))[:n]
#             init ^= int(mask,2)
    
#         return Counter(bin(init))["1"]

        return int(math.sqrt(n))
            