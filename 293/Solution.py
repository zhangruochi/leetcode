"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]
Note: If there is no valid move, return an empty list [].
"""

class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
    
        ans = []
        for i in range(len(s)-1):
            if s[i] == "+" and s[i+1] == "+":
                ans.append(s[:i] + "--" + s[i+2:])
        return ans


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        string = list(s)
        for i in range(len(string)-1):
            if string[i:i+2] == ["+","+"]:
                string[i:i+2] = ["-","-"]
                res.append("".join(string))
                string[i:i+2] = ["+","+"]
        
        return res
            
        