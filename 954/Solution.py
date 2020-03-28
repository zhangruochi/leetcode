from collections import Counter,deque
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = Counter(A)
        sort_key = deque(sorted(count.keys()))
    
            
        while sort_key:
            cur_min = sort_key.popleft()
            value = count.get(cur_min, 0)
                 
            if cur_min < 0:
                s_k = cur_min / 2
            else:
                s_k = cur_min * 2
                    
            
            if cur_min == 0:
                if value % 2 != 0:
                    return False
                
            elif value > 0:        
                if s_k not in count:
                    return False
                count[s_k] -= value
            
            elif value < 0:
                return False
        
            del count[cur_min]

        
        if not count:
            return True
        else:
            return False
        
        
        
        
            
            
            
            
        
        
        