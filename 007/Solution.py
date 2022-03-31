"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        rev = 0
        flag = True

        if x < 0:
            x = -x
            flag = False

        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod

        if not flag:
            rev = -rev

        if  rev <= -2**31  or  rev >= 2 ** 31 - 1:
            return 0
        
        return rev


