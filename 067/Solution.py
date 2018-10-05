"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2) + int(b,2))[2:]

    def addBinary2(self,a,b):

        if len(a) < len(b):
            a,b = b,a

        result,carry,power = 0,0,1
        for i in range(max(len(a),len(b))):

            if i >= len(b):
                value = carry + int(a[-(i+1)])
            else:    
                value = carry + int(a[-(i+1)]) + int(b[-(i+1)])
            
            carry,digit = divmod(value,2)
            
            result = power * digit + result
            power = power * 10

        result =  power * carry + result   


        return str(result)    




if __name__ == '__main__':
    print(Solution().addBinary2(a = "111", b = "1010"))        