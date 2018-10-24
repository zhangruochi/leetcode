class Solution:
    
    def is_ugly(self,n):
        while n % 2 == 0: n //= 2
        while n % 3 == 0: n //= 3 
        while n % 5 == 0: n //= 5
            
        return n == 1
        
    
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        return self.is_ugly(num)