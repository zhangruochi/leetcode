"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4]的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]


限制：

最多会对addNum、findMedian 进行50000次调用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        if not self.array:
            self.array.append(num)
            return 
        
        for i, v in enumerate(self.array):
            if v >= num:
                self.array.insert(i, num)
                return 
        
        if num > self.array[-1]:
            self.array.append(num)
        
        return 
                 
    def findMedian(self) -> float:
        if len(self.array) % 2 == 0:
            return (self.array[len(self.array)//2-1] + self.array[len(self.array)//2]) / 2
        else:
            return self.array[len(self.array)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()