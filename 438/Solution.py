
"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        res = []

        if len(p) > len(s):
            return []
            
        p_dict = defaultdict(int)
        s_dict = defaultdict(int)

        for c in p:
            p_dict[c] += 1
        
        for c in s[:len(p)]:
            s_dict[c] += 1


        diff = {}

        for k in list(p_dict.keys()) + list(s_dict.keys()):
            if p_dict[k] - s_dict[k] != 0:
                diff[k] =  s_dict[k] - p_dict[k]

        if len(diff) == 0:
            res.append(0)
        

        for i in range(len(s) - len(p)):

            prev, new = i, i+len(p)

            if s[prev] in diff:
                diff[s[prev]] -= 1
                if diff[s[prev]] == 0:
                    del diff[s[prev]]
            else:
                diff[s[prev]] = -1

    

            if s[new] in diff:
                diff[s[new]] += 1
                if diff[s[new]] == 0:
                    del diff[s[new]]
            else:
                diff[s[new]] = 1

            if len(diff) == 0:
                res.append(i+1)
        
        return res
            