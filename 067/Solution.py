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


from itertools import zip_longest
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans,carry = "",0
        for a,b in zip_longest(a[::-1],b[::-1],fillvalue=0):
            carry,digit = divmod(int(a)+int(b)+carry,2)
            ans = str(digit) + ans
        if carry:
            ans = str(carry) + ans
        return ans


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = []

        a_bits = list(map(int, a))
        b_bits = list(map(int, b))

        if len(a_bits) < len(b_bits):
            b_bits, a_bits = a_bits, b_bits

        # 使用一个异或门来产生 S，一个与门来产生 C
        def half_adder(a, b):
            return a ^ b, a & b 

        # 全加器可以用两个半加器来构造，将输入端A和B连接到一个半加器上，然后将其和输出信号与进位输入信号分别作为第二个半加器的两个输入，并将两个进位输出信号进行逻辑或运算。全加器的关键路径（critical path，即经历最多逻辑门的路径）经过两个异或门，终止于和位s。假定异或门耗费3个延迟来完成，一个全加器的关键路径上施加的延迟等于
        def full_adder(a, b, c_in):
            s1, c = half_adder(a, b)
            s2, c_out = half_adder(s1, c_in)
            return s2, c | c_out

        c_in = 0
        i = 1
        while i <= len(b_bits):
            b, c_in = full_adder(a_bits[-i], b_bits[-i], c_in)
            print(b,c_in)
            i+=1
            res.append(str(b))
            
        while i <= len(a_bits):
            b, c_in = full_adder(a_bits[-i], 0, c_in)
            i += 1
            res.append(str(b))

        if c_in:
            res.append(str(c_in))

        return "".join(res)[::-1]
        




if __name__ == '__main__':
    print(Solution().addBinary2(a = "111", b = "1010"))        