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
                