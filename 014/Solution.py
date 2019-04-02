"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort(key=len)
        max_length = len(strs[0])
        common_prefix = ""
        for i in range(max_length):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return common_prefix

            common_prefix += strs[0][i]
        return common_prefix

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort(key=len)
        max_length = len(strs[0])
        common_prefix = ""
        for i in range(max_length):
            if "".join([s[i] for s in strs]) != strs[0][i] * len(strs):
                return common_prefix

            common_prefix += strs[0][i]
        return common_prefix

    def longestCommonPrefix3(self,strs):
        if not strs:
            return ""

        for i, letters in enumerate(zip(*strs)):
            if len(set(letters)) > 1:
                return strs[0][:i]

        return min(strs)  


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_length = min(len(string) for string in strs)
        index = 0
        while index < min_length:
            if len(set(string[index] for string in strs)) != 1:
                break
            index += 1
        
        return strs[0][:index]      


if __name__ == '__main__':
    print(Solution().longestCommonPrefix3(["flower", "flow", "flight"]))
