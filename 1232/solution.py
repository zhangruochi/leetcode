class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        start = coordinates[0]
        end = coordinates[-1]
        
        if start[0] - end[0] == 0:
            return len([point[0] for point in coordinates]) == 1
        
        if start[-1] - end[-1] == 0:
            slope = 0
        else:
            slope = float(start[-1] - end[-1]) / float(start[0] - end[0])
        
        b = start[1] - start[0] * slope
                
        def line(slope, b, x):
            """ line equation
            """
            y = slope * x + b
            return y
        
        def in_line(point, slope, b):
            """judge whether the point is in line or not 
            """
            return point[-1] == line(slope,b,point[0])
        
        
        for point in coordinates[1:-1]:
            if not in_line(point, slope, b):
                return False
            
        return True
        