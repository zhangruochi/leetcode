"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for row in range(0,rowIndex):
            result = [1] + [result[i]+result[i+1] for i in range(len(result)-1)] + [1]

        return result    

if __name__ == '__main__':
    print(Solution().getRow(3))        

