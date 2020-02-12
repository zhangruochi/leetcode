from functools import reduce
class Solution:
    def addDigits(self, num: int) -> int:
        
        def get_digits(num):
            res = []
            while num:
                num, re = divmod(num,10)
                res.append(re)
            
            return res
        
        while num >= 10:
            num = reduce(lambda x,y: x+y, get_digits(num))
        
        return num