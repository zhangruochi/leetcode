"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(map(int,str(int("".join(map(str,digits)))+1)))

    def plusOne2(self,digits):
        from functools import reduce
        from collections import deque
        
        prev = reduce(lambda x,y:x*10+y, digits)

        prev += 1    
        result = deque()   
        while prev != 0:
            result.appendleft(prev%10)
            prev = prev // 10

        return list(result) 

    def plusOne3(self,digits):

        result = digits[::-1]
        carry = 1
        for i in range(len(result)):
            result[i] += carry
            carry, result[i] = divmod(result[i],10)
        if carry:
            result.append(carry)

        return result[::-1]     


    def plusOne4(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            carry,digits[i] = divmod(digits[i]+carry,10)
        if carry:
            digits.insert(0,carry)
        return digits   
          




            

if __name__ == '__main__':
    print(Solution().plusOne2([4,3,2,9]))        
