class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        area = 0
        s = []
        while i < len(height):
            if not s or height[i] <= height[s[-1]]:
                s.append(i)
                i+=1
            else:
                t = s.pop()
                while s and s[-1] == t:
                    s.pop()
                if not s: 
                    continue
                print(i,s)
                area += (i-s[-1]-1) * (min(height[i], height[s[-1]]) - height[t])
            
        return area
                
        
            
            
                
                
            
                
            
            
                
            
            
            
                
            
            
            