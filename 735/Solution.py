class Solution(object):
    def asteroidCollision(self, asteroids):
        res = []
        for a in asteroids:
            
            while res and res[-1] > 0 and a < 0:
                if res[-1] < -a:
                    res.pop()
                elif res[-1] == -a:
                    res.pop()
                    break
                elif res[-1] > -a:
                    break
            else:
                res.append(a)
        
        return res
                    
                    
            
                
        
        