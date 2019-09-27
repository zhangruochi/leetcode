"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if not s or numRows == 1: return s
        
        res = [[] for i in range(numRows)]
        index = 0
        i = 0
        while index < len(s):
            while index < len(s) and i < numRows:
                res[i].append(s[index])
                i += 1
                index += 1
            else:
                i -= 1
            
            
            while index < len(s) and i > 0:
                i -= 1
                res[i].append(s[index])
                index += 1
            else:
                i += 1
            
        
        return "".join(["".join(item) for item in res])