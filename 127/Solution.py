"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

### Time Limit Exceeded

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        visited = set()
        ans = float("inf")
        flag = False
        def rec_dfs(beginWord,steps,visited):
            nonlocal ans,flag
            
            if beginWord == endWord:  
                ans = min(ans,steps)
                flag = True
                return 

    
            for i in range(len(wordList)):
                for new in "abcdefghijklmnopqrstuvwxyz":
                    s = beginWord[0:i] + new + beginWord[i+1:]
                    if s in wordSet and s not in visited:
                        visited.add(s)
                        steps += 1
                        rec_dfs(s,steps,visited)
                        visited.discard(s)
                        steps -= 1
            return 
                        
                    
        rec_dfs(beginWord,1,visited)
        if not flag:
            return 0
        
        return ans




from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        queue =deque([beginWord])
        step,l = 0,len(beginWord)
        while queue:
            step += 1
            size = len(queue)
            while size:
                cur = queue.popleft()
                for i in range(l):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        new = cur[:i] + char + cur[i+1:]

                        if new not in wordSet:
                            continue

                        if new == endWord:
                            return step + 1

                        queue.append(new)
                        wordSet.discard(new)
                size -= 1
             
        return 0
                    