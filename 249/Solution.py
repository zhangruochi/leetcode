"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

from collections import defaultdict

class Solution:
    
    def is_shift(self,a,b):
        if not a or not b or len(a) != len(b):
            return False
       
        if len(a) == 1 and len(b) == 1:
            return True
        
        base = (ord(a[0]) - ord(b[0])) % 26
        
        for char_a,char_b in zip(a,b):
            if (ord(char_a) - ord(char_b))%26 != base:
                return False
            
        return True
        
        
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if not strings:
            return []
        
        table = defaultdict(list)
        first = strings.pop()
        table[first].append(first)

        while strings:
            cur = strings.pop()
            for key in table.keys():
                if is_shift(cur,key):
                    table[key].append(cur)
                    continue
            table[cur] = [cur]            
        return list(table.values())

class Solution:
    
    def transform(self,a):
        def func(char,base = a[0]):
            return chr((ord(char) - ord(base))%26 + ord('a'))

        return "".join(map(func,a))    


    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if not strings:
            return []
        
        table = {}       
        for string in strings:
            num = self.transform(string)
            if num not in table:
                table[num] = [string]
            else:
                table[num].append(string)    

        return list(table.values())        


if __name__ == '__main__':
    a = "abc"
    b = "bcd"


    #c,d = "ab","za"

    solution = Solution()
 
    print(solution.transform(a))
    print(solution.transform(b))


