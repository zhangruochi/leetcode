"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = Counter(s)
        
        
        for index,char in enumerate(s):
            if table[char] == 1:
                return index
        
        return -1


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = [0]*26
        for char in s:
            table[ord(char)-ord('a')] += 1
            
        
        for index,char in enumerate(s):
            if table[ord(char)-ord('a')] == 1:
                return index
        
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        count_dict = Counter(s)

        for i, c in enumerate(s):
            if count_dict[c] == 1:
                return i
        
        return -1