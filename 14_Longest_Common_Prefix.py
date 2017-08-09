#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com


"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix_1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_length = min([len(_) for _ in strs])
        result = ""

        for i in range(min_length):
            index = 0
            for string in strs:
                if index == 0:
                    chr_ = string[i]
                    index += 1
                else:
                    if chr_ == string[i]:
                        continue
                    else:
                        return result
            result += chr_

        return result

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if len(prefix) == 0:
                    return ""
        return prefix



if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["abc", "abcdf", "abrtf", "a"]))
