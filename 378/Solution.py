"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
import heapq
class Solution:

    # time complexity O(nlogn) and space cmplexity is O(n*2)
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lists_ = []
        for row in matrix:
            lists_ += row
        lists_.sort()
        return lists_[k-1]


    # time complexity O(nk) and space cmplexity is O(n)    
    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        pointers = [0] * n
        count = 0
        while True:
            min_,min_index = float("inf"),-1
            for index,point in enumerate(pointers):
                if point < n:
                    tmp_min = matrix[index][point]
                    if tmp_min < min_: 
                        min_ = tmp_min
                        min_index = index
            pointers[min_index] += 1
            count += 1
            if count == k:
                return min_



import heapq

class MyItem:
    def __init__(self,num,row,column):
        self.num = num
        self.row = row
        self.column = column
    
    def __lt__(self,item):
        return self.num < item.num
    
    def __repr__(self):
        return "{}".format(self.num)
        

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        heap = [ MyItem(matrix[0][j],0,j) for j in range(n)]
        heapq.heapify(heap)

        for i in range(k):
            item = heapq.heappop(heap)
            num, row, column = item.num, item.row, item.column
            if row+1 < n:
                heapq.heappush(heap,MyItem(matrix[row+1][column],row+1,column))
        return num 









