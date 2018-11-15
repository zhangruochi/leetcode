"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?

"""


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        
        while True:
            n,res = divmod(n,3)
            if res != 0:
                break
        return n == 0 and res == 1

import math
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        epsilon = 10e-15
        res = math.log(n)/math.log(3)
        return  abs(res - round(res)) <= epsilon
    
                
