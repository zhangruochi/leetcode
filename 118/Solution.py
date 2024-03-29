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

    
    def generate3(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            if not res:
                res.append([1])
            else:
                tmp = [1]
                for i in range(len(res[-1])-1):
                    tmp.append(res[-1][i]+res[-1][i+1])
                tmp.append(1)
                res.append(tmp)
        return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1], [1,1]]

        if numRows == 0 :
            return [[]]

        if numRows <= 2:
            return res[: numRows]


        for i in range(3, numRows+1):
           res.append( [1] + [ a+b  for a, b in zip(res[-1][:-1], res[-1][1:])] + [1] )

        return res
        
        

if __name__ == '__main__':
    print(Solution().generate2(5))         