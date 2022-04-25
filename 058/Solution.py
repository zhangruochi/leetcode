"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution:
    
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        else:
            return len(s.split(" ")[-1])
    
            
    def lengthOfLastWord2(self, s):

        last = True
        i = len(s) -1
        count = 0

        while i >= 0:
            if s[i] == ' ' and last:
                i -= 1
            elif s[i] == ' ' and (not last):
                return count
            else:
                count += 1
                last = False
                i -= 1

        return count

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        flag = True
        for i in range(len(s)-1,-1,-1):
            if flag and s[i] == ' ':
                continue
            
            if  ord('a') <= ord(s[i]) <= ord('z') or ord('A') <= ord(s[i]) <= ord('Z'):
                count += 1
                flag = False
            
            if s[i] == ' ':
                break
        
        return count
      

class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        return len(s.strip().split()[-1])

