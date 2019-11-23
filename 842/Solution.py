class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        res = []
        
        max_ = 2 ** 31 -1
        
        def helper(s, path):
            nonlocal res
            
            if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
                return False
            
            if len(path) >= 3 and s == "":
                res = path[:]
                return True
            
            
            for i in range(len(s)):
                cur_str = s[:i+1]
                
                if cur_str[0] == '0' and len(cur_str) > 1:
                    continue
                
                if int(cur_str) > max_:
                    continue
                
                path.append(int(cur_str))
                if helper(s[i+1:],path):
                    return True
                path.pop()
                
            return False
                
        helper(S,[])
            
        return res
                
                
        