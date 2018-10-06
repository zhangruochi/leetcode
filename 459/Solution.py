"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.


Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times.
"""


class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # repeated times
        if not len(s):
            return False

        k = 2
        while len(s) // k >= 1:
            if len(s) % k != 0:
                k += 1
                continue
 
            if s == s[0:len(s)//k] * k:
                return True

            k+=1    

        return False
                
                


     

if __name__ == '__main__':
    print(Solution().repeatedSubstringPattern("ababab"))
            
