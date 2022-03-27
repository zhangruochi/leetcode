"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        push = ("(","{","[")
        pop = (")","}","]")

        stack = []
        for char in s:
            if char in push:
                stack.append(char)
            elif char in pop:
                if stack == []:
                    return False
                elif pop.index(char) != push.index(stack[-1]):
                    return False
                else:
                    stack.pop()    
        
        if len(stack):
            return False      

        return True    

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        table = {"(":")","[":"]","{":"}"}
        stack = []
        for char in s:
            if char in table:
                stack.append(char)
            else:
                if not stack or char != table[stack.pop()]:
                    return False
        if stack:
            return False
        
        return True      



class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        char_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        flag = True

        for c in s:
            if c in char_map:
                stack.append(c)
            else:
                if stack and stack[-1] in char_map and char_map[stack[-1]] == c:
                    stack.pop()
                else:
                    flag = False
                    break
        
        if len(stack) > 0:
            flag = False

        return flag

if __name__ == '__main__':
    print(Solution().isValid(""))

