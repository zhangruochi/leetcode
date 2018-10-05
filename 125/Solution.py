"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s):
        import re
        """
        :type s: str
        :rtype: bool
        """
        return "".join(re.split("\W+",s.lower()))== "".join(re.split("\W+",s.lower()))[::-1]

    def getNormalStr(self,str):
        result = ""
        for char in str.lower():
            if '0' <= char and char <= '9' or char >= 'a' and char <= 'z':
                result += char
        return result        
 
    def isPalindrome2(self,s):
        s = self.getNormalStr(s)
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True        



        
            

if __name__ == '__main__':
    print(Solution().isPalindrome2("A man, a plan, a canal: Panama"))        
        