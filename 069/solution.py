"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        for i in range(1, x//2+2):
            if i * i == x:
                return i
            elif i * i > x:
                return i-1
        
        return -1

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        def binarySerach(low,high,x):
            if low > high:
                return -1
            
            mid =  low + (( high - low ) // 2)
            
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                return binarySerach(mid+1, high, x)
            else:  # mid ** 2 > x
                if mid == 1 or (mid - 1) ** 2 < x:
                    return mid-1
                else:
                    return binarySerach(low, mid-1, x)
        
        return binarySerach(1,x,x)


class Solution:
    def mySqrt(self, x: int) -> int:

        def square(x):
            return x * x

        def helper(l, r, target):
            if l > r:
                return -1

            mid  = (r + l ) // 2

            if square(mid) > target:
                return helper(l, mid-1, target)
            else:
                if square(mid + 1) > target:
                    return mid
                else:
                    return helper(mid+1, r, target)


        return helper(0, x, x)