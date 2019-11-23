class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def helper(num_str,path):
            if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
                return False
            
            if not num_str and len(path) >= 3:
                return True
            
            
            for i in range(len(num_str)):
                cur_str = num_str[:i+1]
                
                # 减枝
                if (cur_str[0] == '0' and len(cur_str) != 1):
                    continue
                    
                path.append(int(cur_str))
                if helper(num_str[i+1:],path):
                    return True
                path.pop()
            
            return False
        
        return helper(num,[])


