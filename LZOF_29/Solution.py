"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []

        res = []

        directions = ((0,1),(1,0),(0,-1),(-1,0))
        upper_n,upper_m = len(matrix), len(matrix[0])
        low_n,low_m, n, m = 0, 0, 0, 0

        index = 0
        while True:

            d = directions[index % 4]
       
            while low_n <= n < upper_n and low_m <= m < upper_m:
                res.append(matrix[n][m])
                n += d[0]
                m += d[1]

            if m >= upper_m:
                m -= 1

                low_n += 1
                n += 1
            
            if n >= upper_n:
                n -= 1

                upper_m -= 1
                m -= 1

            if m < low_m:
                m += 1

                upper_n -= 1
                n -= 1
            
            if n < low_n:
                n += 1
                
                low_m += 1
                m += 1
            
            # print([n,m, low_n, upper_n, low_m, upper_m])
            index  += 1

            if index > len(matrix[0]) * len(matrix):
                break

        return res