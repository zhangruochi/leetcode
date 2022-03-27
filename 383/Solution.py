"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        from collections import Counter

        r_dict = Counter(ransomNote)
        m_dict = Counter(magazine)

        for k,v in r_dict.items():
            if k not in m_dict or v > m_dict[k]:
                return False
    
        return True