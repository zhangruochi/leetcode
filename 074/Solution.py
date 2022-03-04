"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""


def two2one(i, j, n):
    return i * n + j

def one2two(k, n):
    i = k // n
    j = k % n
    return [i, j]

def binary_search(matrix, target, l, r):
    n = len(matrix[0])
    l_, r_ = two2one(l[0], l[1], n), two2one(r[0], r[1], n)

    if l_ > r_:
        return False

    mid = (l_ + r_) // 2
    mid_i, mid_j = one2two(mid, n)

    if matrix[mid_i][mid_j] == target:
        return True
    elif matrix[mid_i][mid_j] > target:
        return binary_search(matrix, target, l,  one2two(mid -1, n))
    else:
        return binary_search(matrix, target, one2two( mid +1, n), r)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        return binary_search(matrix, target, [0,0], [len(matrix)-1, len(matrix[0])-1])




## 

def search_column(matrix, target, l, r):
    if l > r:
        return -1
    
    mid = (l + r) // 2

    if matrix[mid][0] <= target:
        if mid+1 < len(matrix) and matrix[mid+1][0] > target:
            return mid
        elif mid+1 >= len(matrix):
            return mid
        else:
            return search_column(matrix, target, mid+1, r)
    else:
        return search_column(matrix, target, l, mid-1)

def seach_row(matrix, target, row, l, r):
    if l > r:
        return False
    
    mid = (l + r) // 2

    if matrix[row][mid] == target:
        return True
    elif matrix[row][mid] < target:
        return seach_row(matrix, target, row, mid+1, r)
    else:
        return seach_row(matrix, target, row, l, mid-1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False


        row = search_column(matrix, target, 0, len(matrix)-1)

        if row == -1:
            return False

        return seach_row(matrix, target, row, 0, len(matrix[0])-1)

