"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def is_capital(char):
            return 'A' <= char and char <= 'Z'
        
        
        count = 0
        for char in word:
            if is_capital(char):
                count += 1
            
        if count == 0:
            return True
        elif count == 1 and is_capital(word[0]):
            return True
        elif count == len(word):
            return True
        else:
            return False
        