class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if not points: return 0
        
        times = 0
        for i in range(1,len(points)):
            length1, length2 = points[i][0]-points[i-1][0],points[i][1]-points[i-1][1]
            diff = abs(length1-length2)
            times += diff
            times += (max(abs(length1),abs(length2)) - diff)
        
        return times
            
            