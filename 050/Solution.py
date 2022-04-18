"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        memo = {}
        
        def rec_pow(x,n,memo):
            if n in memo:
                return memo[n]
            
            if n == 0:
                return 1
            if n == 1:
                return x
        
            memo[n] = rec_pow(x,n//2,memo) * rec_pow(x,n-n//2,memo)
            return memo[n]
        
        if n < 0:
            n = -n
            return 1/rec_pow(x,n,memo)
        else:
            return rec_pow(x,n,memo)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        memory = {}
        
        def helper(x,n):
            nonlocal memory 
            if n == 1:
                return x
            
            if n in memory:
                return memory[n]
            
            if n % 2 == 0:
                res =  helper(x,n//2) * helper(x, n//2)
            else:
                res =  helper(x,n//2) * helper(x, n//2 + 1)
            
            memory[n] = res
            
            return res
        
        return helper(x,abs(n)) if n > 0 else 1 / helper(x,abs(n))


class Solution:
    def myPow(self, x: float, n: int) -> float: 

        def helper(x, n):
            if n < 0:
                return 1/self.myPow(x, -n)
            if n == 0:
                return 1
            if n == 1:
                return x
            
            y = helper(x, n//2)

            if n % 2 == 0:
                return y*y
            else:
                return y*y*x

        return helper(x, n)
        