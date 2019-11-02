"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        table = {
            '0':[""],
            '1':["*"],
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        ans = []
        cur = ""
        
        def dfs(l,cur):
            if l == len(digits):
                ans.append(cur)
                return 
            
            for c in table[digits[l]]:
                dfs(l+1,cur+c)
        
        def backtrack(l):
            nonlocal cur
            if l == len(digits):
                ans.append(cur)
                return 
            
            for c in table[digits[l]]:
                cur += c
                backtrack(l+1)
                cur = cur[:-1]
                
        
        backtrack(0)
        #dfs(0,"")
        return ans


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        graph = {   '2': ['a','b','c'],
                    '3': ['d','e','f'],
                    '4': ['g','h','i'],
                    '5': ['j','k','l'],
                    '6': ['m','n','o'],
                    '7': ['p','q','r','s'],
                    '8': ['t','u','v'],
                    '9': ['w','x','y','z']
                }
        
        res = []
        
        def helper(digits,path):
            
            if not digits:
                res.append(path)
                return 
            
            for char in graph[digits[-1]]:
                item = digits.pop()
                helper(digits,path+char)
                digits.append(item)
                
            return res
            
        
        return helper(list(digits)[::-1],"")