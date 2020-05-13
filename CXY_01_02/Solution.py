"""
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true 
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false
说明：

0 <= len(s1) <= 100
0 <= len(s2) <= 100


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-permutation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import Counter
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:

        count1 = Counter(s1)
        count2 = Counter(s2)

        if len(count1) != len(count2):
            return False

        for k,v in count1.items():
            if v != count2.get(k, -1):
                return False
        
        return True
