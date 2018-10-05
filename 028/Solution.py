"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        haystack_len = len(haystack)
        needle_len = len(needle)

        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i
        return -1

    def partial(self, pattern):
        next = [0]
        for i in range(1,len(pattern)):
            j = next[i - 1]

            while j > 0 and pattern[j] != pattern[i]:
                j = next[j - 1]

            next.append(j + 1 if pattern[i] == pattern[j] else j)

        return next

    def strStr2(self, haystack, needle):
        if not needle:
            return 0

        next, j = self.partial(needle), 0
        print(next)

        lenth = len(needle)

        for i in range(len(haystack)):

            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == lenth:
                return i - j + 1

        return -1       
         
if __name__ == '__main__':
    print(Solution().strStr2(haystack="mississippi", needle="issip"))
