"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        index = 0

        while num > 0:

            rem = num % 2
            num = num >> 1
            index += 1

            if rem == 1 and num != 0:
                return False

            elif rem == 1 and num == 0 and index % 2 == 0:
                return False

        return True

    def isPowerOfFour2(self, num):
        import math
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        a = math.log(num, 4)
        return True if int(a) == a else False

    def isPowerOfFour3(self, num):
        return bin(num)[2:].count('1') == 1 and bin(num)[2:].count('0') % 2 == 0

    def isPowerOfFour4(self, num):
        return num > 0 and (num & (num - 1)) == 0 and \
            ((num & 0b01010101010101010101010101010101) == num)


if __name__ == '__main__':
    print(Solution().isPowerOfFour(64))
