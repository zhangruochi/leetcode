"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:

Input: "()"
Output: True
Example 2:

Input: "(*)"
Output: True
Example 3:

Input: "(*))"
Output: True
Note:

The string size will be in the range [1, 100].
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack_l, stack_s = [], []
        
        for i in range(len(s)):
            if s[i] == "(":
                stack_l.append(i)
            elif s[i] == "*":
                stack_s.append(i)
            else:
                if stack_l:
                    stack_l.pop()
                elif stack_s:
                    stack_s.pop()
                else:
                    return False
        
        if len(stack_s) < len(stack_l):
            return False
    
        
        while stack_l:
            if stack_l.pop() > stack_s.pop():
                return False
    
        
        return True
                    
                    
                    
                    
            
        
        
        
        