"""
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) + (n % 2)
            n = n >> 1
        return result

    def reverseBits2(self, n):
        n = '{0:032b}'.format(n)
        return int(n[::-1], 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits2(43261596))
