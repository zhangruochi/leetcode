"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append([1,""])
        num = ""
        for char in s:
            if char.isdigit():
                num += char
            elif char == "[":
                stack.append([int(num),""])
                num = ""
            elif char == "]":
                k,str_ = stack.pop()
                stack[-1][1] += str_ * k
            else:
                stack[-1][1] += char

        return stack[-1][1]




class Substring:
    def __init__(self,num,s):
        self.num = num
        self.s = s

class Solution:
    def decodeString(self, s: str) -> str:
        
        root = Substring(1,"")
        stack = [root]
        
        i,num = 0,""

        for char in s:
            if char.isdigit():
                num += char
            elif char == "[":
                stack.append(Substring(int(num),""))
                num = ""
            elif char == "]":
                sub = stack.pop()
                stack[-1].s += sub.num * sub.s
            else:
                stack[-1].s += char
        
        return root.s * root.num
            
        