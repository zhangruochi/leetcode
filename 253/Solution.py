"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

class Solution:
    ## 时间复杂度高
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return len(intervals)
        
        max_count = 0
        intervals.sort(key = lambda x:x.start)
        for start in (interval.start for interval in intervals):
            count = 0
            for interval in intervals:
                if start < interval.start:
                    break
                if start >= interval.end:
                    continue
                    
                if start >= interval.start and start < interval.end:
                    count += 1
            if count > max_count:
                max_count = count
        return max_count


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts,ends = [],[]
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()
        
        room,end = 0,0
        for start in starts:
            if start < ends[end]: room += 1
            else: end += 1
        return room   


# 扫描线算法
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts,ends = [],[]
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()
        
        room,end = 0,0
        for start in starts:
            if start < ends[end]: room += 1
            else: end += 1
        return room



class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        points = []
        for interval in intervals:
            points.append((interval.start,1))
            points.append((interval.end,-1))
        
        points.sort()
        count,room = 0,0
        for _,delta in points:
            count += delta
            room = max(room,count)

        return room



        
        
