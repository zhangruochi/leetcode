#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com


"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        TABLE = {")": "(","]": "[","}":"{"}

        stack = []
        for _ in s:
            if _ in TABLE.values():
                stack.append(_)
            else:
                if not stack:
                    return False
                elif stack.pop() != TABLE[_]:
                    return False   

        if not stack:
            return True

        return False



if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))        
