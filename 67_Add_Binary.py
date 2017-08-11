#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""

class Solution(object):
    def addBinary_1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2) + int(b,2))[2:]

     
    def addBinary(self,a,b):
        if len(a) == 0; return b
        if len(b) == 0; return a

        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'    
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1]) + "0"
        else:
            return self.addBinary(a[0:-1],b[0:-1]) + "1"
                    


if __name__ == '__main__':
    solution = Solution()  
    print(solution.addBinary("0","1"))      