"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""

class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if num.count("8") == len(num) or num.count("1") == len(num) or num.count("0") == len(num):
            return True
        
        dict_table = {"6":"9","9":"6","8":"8","1":"1","0":"0"}
        
        if num[0] == "0":
            return False
        
        if len(num) % 2 != 0:
            if not num[len(num)//2] == "8" and not num[len(num)//2] == "1" and not num[len(num)//2] == "0":
                return False
        
        for i in range(len(num)//2):
            
            if not num[i] in dict_table or dict_table[num[i]] != num[-i-1]:
                return False
        
        return True


    def isStrobogrammatic(self, num):
        dict_table = {"6":"9","9":"6","8":"8","1":"1","0":"0"}
        if num[0] == "0":
            return False

        for i in range(len(num)//2):
            if num[i] not in dict_table or dict_table[num[i]] != num[-i-1]:
                return False
        return True    
                       
