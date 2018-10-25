"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index_c = []
        for index,char in enumerate(S):
            if char == C:
                index_c.append(index)

        result = [i for i in range(index_c[0],0,-1)]
        for prev,cur in zip(index_c,index_c[1:]):
            length = cur - prev
            tmp = []
            if length % 2 != 0:
                for i in range(1,length//2+1):
                    tmp.append(i)
                for i in range(length//2,0,-1):
                    tmp.append(i)
            else:
                for i in range(1,length//2+1):
                    tmp.append(i)
                for i in range(length//2-1,0,-1):
                    tmp.append(i)
            result.append(0)
            result.extend(tmp)
        result.append(0)
        for i in range(1,len(S)-index_c[-1]):
            result.append(i)
        
        return result