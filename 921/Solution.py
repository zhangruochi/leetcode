"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
"""
from collections import deque
class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for char in S:
            
            if stack and stack[-1] == "(" and char == ")":
                stack.pop()
            else:
                stack.append(char)
        return len(stack)


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        count = 0
        stack = []
        for char in S:
            if char == "(":
                stack.append(char)
                count += 1
            elif char == ")" and stack and stack[-1] == "(":
                stack.pop()
                count -= 1
            else:
                count += 1
        
        return count
                
                
                    