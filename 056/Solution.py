"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""



# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# class Solution:
#     def merge(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """
#         ans,stack,points = [],[],[]
#         for interval in intervals:
#             points.append([interval.start,0])
#             points.append([interval.end,1])
#         points.sort()
        
#         for time,_ in points:
#             if not _:
#                 stack.append(time)
#             else:
#                 start = stack.pop()
#                 if not stack:
#                     ans.append([start,time])
        
#         return ans


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        
        intervals.sort(key = lambda x : x[0])
        
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                if stack[-1][1] >= interval[0]:
                    tmp = stack.pop()
                    stack.append([tmp[0],max(tmp[1],interval[1])])
                else:
                    stack.append(interval)
        
        return stack