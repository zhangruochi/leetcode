"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(s,left,right):
            if left > right or left < 0 or right < 0:
                return
            
            if left == 0 and right == 0:
                ans.append(s)
            
            backtrack(s+"(",left-1,right)
            backtrack(s+")",left,right-1)
            
        
        backtrack("",n,n)
        return ans