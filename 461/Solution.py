"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are dif
"""


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        def bit_count(number):
            count = 0
            while number:
                number = number & (number - 1)
                count += 1
            return count

        return bit_count(x ^ y)


if __name__ == '__main__':
    print(Solution().hammingDistance(1, 4))
