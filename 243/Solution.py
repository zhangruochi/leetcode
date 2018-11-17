"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1,l2 = 0,0
        flag1,flag2 = False,False
        distance = float("inf")
        for index,word in enumerate(words):
            if word == word1:
                l1 = index
                flag1 = True
            if word == word2:
                l2 = index
                flag2 = True
            
            if flag1 and flag2:
                distance = min(distance, abs(l1-l2))

        return distance
            
            
            
                
            
        