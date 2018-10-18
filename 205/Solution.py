"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_map = {}
        value_set = set()

        for char_s,char_t in zip(s,t):
            if char_s in char_map and char_map[char_s] != char_t:
                return False

            if char_s not in char_map and char_t in value_set:
                return False

            if char_s not in char_map:
                char_map[char_s] = char_t
                value_set.add(char_t) 

        return True                    















