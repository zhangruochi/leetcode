import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        f = lambda point: -(point[0]**2 + point[1]**2)**0.5
        
        heap  = []
        for point in points:
            heapq.heappush(heap,(f(point),point))
            if len(heap) > K:
                heapq.heappop(heap)
        
        return [item[1] for item in heap]