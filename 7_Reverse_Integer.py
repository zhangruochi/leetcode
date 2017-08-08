#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse_me(self, x):
        """
        :type x: int
        :rtype: int
        """
        positive = limit = 2**31 - 1
        negative = -(positive + 1)

        if x == 0:
            return 0

        if x > 0:
            x = str(x)[::-1]
            for index in range(len(x)):
                if x[index] != 0:
                    break
            result = int(x[index:])    
            if result > positive:
                return 0

        elif x < 0:
            x = str(x)[::-1][:-1]
            for index in range(len(x)):
                if x[index] != 0:
                    break
            result = int("-"+x[index:])
            if result < negative:
                return 0

        return result

    
    def reverse(self,x):
        MAX = 0x7fffffff
        MIN = -0x80000000
        
        total = 0

        while(x!=0):
            remainder = x % 10
            x = x / 10
            total = total * 10 + remainder
            
            if (total > MAX || total < MIN):
                return 0



if __name__ == '__main__':
    solution = Solution()                    
    print(solution.reverse(1000000003))

                





