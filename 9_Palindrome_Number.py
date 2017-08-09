#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com

"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        flag = 1
        index = 0

        while(flag <= x):
            flag *= 10
            index += 1

        flag /= 10

        for i in range(index // 2):
            quotient = x // flag
            remainder = x % 10

            if quotient != remainder:
                return False

            x = (x - quotient * flag - remainder) / 10
            flag /= 100

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(-1))
