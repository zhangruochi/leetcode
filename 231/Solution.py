"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n == 1):
            return True

        power = 0
        while True:
            if (2 << power == n):
                return True
            if (2 << power) > n:
                return False

            power += 1

    def isPowerOfTwo2(self, n):
        if(n < 0):
            return False
        return bin(n).count('1') == 1


    def isPowerOfTwo4(self, n):  
        return n>0 and (n & (n-1)) == 0 


if __name__ == '__main__':
    print(Solution().isPowerOfTwo3(16))
