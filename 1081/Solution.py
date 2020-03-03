"""
1081. Smallest Subsequence of Distinct Characters
Medium

271

52

Add to List

Share
Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

Example 1:

Input: "cdadabcc"
Output: "adbc"
Example 2:

Input: "abcd"
Output: "abcd"
Example 3:

Input: "ecbacba"
Output: "eacb"
Example 4:

Input: "leetcode"
Output: "letcod"
 

Constraints:

1 <= text.length <= 1000
text consists of lowercase English letters.
"""



from collections import defaultdict
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        count = defaultdict(int)
        for c in text:
            count[c] += 1
        
        visited = set()
        stack = []
        
        for c in text:
            if c in visited:
                count[c] -= 1
                continue
        
 
            while stack and stack[-1] > c and count[stack[-1]] > 0:
                visited.remove(stack.pop())
                    
            stack.append(c)
            visited.add(c)
            count[c] -= 1
                    
                
        return "".join(stack)
                
            
    # "cdadabcc"
    # c = [0,6,7]
    # b = [5]
    # d = [1,3]
    # a = [2,4]
    
    