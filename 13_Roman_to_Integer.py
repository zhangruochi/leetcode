#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com


"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_number = {"I": 1, "V": 5, "X": 10,
                        "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 1:
            return roman_number[s]

        result = 0
        for i in range(len(s) - 1):
            if roman_number[s[i]] < roman_number[ s[i + 1] ]:
                result -= roman_number[s[i]]
            else:
                result  +=  roman_number[s[i]]

        result += roman_number[s[-1]]

        return result

if __name__ == '__main__':
    solution = Solution() 
    print(solution.romanToInt("MCMXCVI"))           
