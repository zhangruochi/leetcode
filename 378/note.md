## 思路

- 最简单方法：
    - 所有元素拼接在一起，然后直接排序，再返回第k个元素
    - time complexity: O(n^2logn), space complexity: O(n^2)


- 降低空间复杂度
    - 采用 n 个指针同时遍历每个row, 最小元素的 point += 1
    - time complexity: nk, space complexity: O(n)

- 利用minheap来解决， 将这些数字放进堆里， 弹出k次 那么就能得到题目想要的数字。

    - 将第一行的所有元素放入heap里。
    - 循环k-1次：每一次将最小的元素弹出， 因此需要知道每个元素的在矩阵中的坐标， （可以建立一个类来存放）。然后将被弹出元素的同一列的下一个元素放入heap里。
    - 注意 python 里 heapq 元素的定义。

```Python
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
```