#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""


class Solution(object):
    def lengthOfLastWord_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        return len(s.strip(" ").split(" ")[-1])

    def lengthOfLastWord(self, s):
        length = len(s)

        if length == 0:
            return 0

        # 去掉结尾空格符号
        while length > 0:
            if s[length - 1] == " ":
                length -= 1
            else:
                break    


        s = s[:length]

        counter = 0
        for char in s:
            if char == " ":
                counter = 0
            else:
                counter += 1

        return counter


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord("a"))
