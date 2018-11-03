"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True
Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:

The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class Solution:
    def check(self,s):
        return s == s[::-1]
          
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
    
        if s == s[::-1]:
            return True
        else:
            l,h = 0, len(s)-1
            while l < h:
                if s[l] != s[h]:
                    if self.check(s[l+1:h+1]) or self.check(s[l:h]):
                        return True
                    else:
                        return False
                l += 1; h -= 1
        return True