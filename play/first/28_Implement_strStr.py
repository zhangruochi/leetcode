#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com

"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution(object):
    def strStr_me(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    
    def strStr(self, haystack, needle):
        length = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+length] == needle:
                return i
        return -1            


