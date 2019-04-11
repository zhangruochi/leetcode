"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        max_ = 1
        sub_set = set([s[i]])
        for j in range(1,len(s)):
            if s[j] not in sub_set:
                sub_set.add(s[j])
            else:
                while s[i] != s[j]:
                    sub_set.remove(s[i])
                    i+=1
                i += 1
            max_ = max(len(sub_set),max_)
        return max_
            
            
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,j,max_= 0,0,0
        visited = set()
        while j < len(s):
            if s[j] not in visited:
                visited.add(s[j])
            else:
                index = s[i:j].index(s[j])
                for k in range(i,i+index+1):
                    visited.discard(s[k])
                i = i+index + 1
                visited.add(s[j])
                    
            max_ = max(max_,len(visited))
            j += 1
        return max_
