"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
"""

from operator import add
from functools import reduce


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return reduce(add, map(int, bin(n)[2:]))

    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

    def hammingWeight3(self, n):
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n //= 2
        return count

    def hammingWeight4(self, n):
        mask = 1
        count = 0
        for i in range(32):
            if n & mask != 0:
                count += 1
            mask = mask << 1

        return count

    def hammingWeight5(self, n):
        count = 0
        while n != 0:
            n &= n - 1
            count += 1

        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight5(11))
