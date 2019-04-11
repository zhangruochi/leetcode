"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        word = ""
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != " ":
                word += s[i]
                i += 1
            
            ans += word[::-1]
            word = ""
            while i < len(s) and s[i] == " ":
                ans += s[i]
                i += 1
        return ans


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return " ".join( [w[::-1]  for w in s.split(" ")])
        
        