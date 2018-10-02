"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
import sys
sys.setrecursionlimit(1500)

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        def iter(num,result):
            if num == 0:
                return result
            else:
                result.append([1] + [result[-1][i]+result[-1][i+1] for i in range(len(result)-1)] + [1])
                return  iter(num-1,result)     

        result = [[1]]
        num = numRows-1
        
        return iter(num,result)

    def generate2(self,numbers):
        if numbers == 0:
            return []
        result = [[1]]   
        for i in range(1,numbers):
            tmp = [1] + [result[-1][j] + result[-1][j+1] for j in range(len(result[-1])-1)] + [1]
            result.append(tmp)
        return result    



if __name__ == '__main__':
    print(Solution().generate2(5))         