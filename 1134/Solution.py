from functools import reduce
class Solution:
    def isArmstrong(self, N: int) -> bool:
        if N == 0:
            return True
        
        num_digits = 0
        a = N
        while a:
            a //= 10
            num_digits += 1
        
        
        def map_func(digit):
            return int(digit)**num_digits
        
        return reduce(lambda x,y: x+y,map(map_func,str(N))) == N
    
    
            