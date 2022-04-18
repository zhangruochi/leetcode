class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        def rec_str(s,ans):
            if len(s) < 1:
                return ans
            return rec_str(s[:-1],ans+s[-1])
        return rec_str(s,ans)
        

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length // 2):
            s[i], s[length-i-1] = s[length-i-1], s[i]