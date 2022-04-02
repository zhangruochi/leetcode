"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        

        num1 = list(map(int, num1))
        num2 = list(map(int, num2))

        res = 0
        mul = 1

        def helper(i, num1):
            res = 0
            carry = 0
            mul = 1
            for j in num1[::-1]:
                carry, mod = divmod (i * j + carry, 10)
                res = res + mod * mul 
                mul *= 10

            if carry:
                res = carry * mul + res
            
            return res

        for i in num2[::-1]:
            res += helper(i, num1) * mul
            mul *= 10
        
        return str(res)