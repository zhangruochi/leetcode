"""
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。



示例1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10]重叠。
示例 3：

输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]
示例 4：

输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]
示例 5：

输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = len(intervals)
        for i,interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                index = i
                break
        
        
        intervals = intervals[:index] + [newInterval] + intervals[index:]
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                if interval[0] <= stack[-1][1]:
                    tmp = stack.pop()
                    stack.append([tmp[0],max(interval[1], tmp[1])])
                else:
                    stack.append(interval)
        
        return stack
                

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])

        res = []
        i = 0

        while i < len(intervals):

            start = intervals[i][0]
            end = intervals[i][1]
                
            while i < len(intervals)-1 and end >= intervals[i+1][0]:
                end = max(end, intervals[i+1][1])
                i += 1
            else:
                res.append([start, end])
            
            i += 1
        return res