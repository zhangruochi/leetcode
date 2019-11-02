def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        
        def dfs(cur,index,count):
            if count > 4:
                return 
            if count == 4 and index == len(s):
                ans.append(cur)
                return 
            
            for i in range(1,4):
                end = index + i
                if end > len(s): break
                    
                if s[index:end][0] == "0" and i > 1: 
                    break
                if int(s[index:end]) > 255:
                    break
                
                if count < 3:
                    next_cur = cur + s[index:end] + "."
                else:
                    next_cur = cur + s[index:end]
                    
                dfs(next_cur,index+i,count+1)
                         
        dfs("",0,0)
        return ans

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:    
        res = []
        if not s:
            return res
        
        def check(ip):
            if ip[0] == '0' and len(ip) > 1:
                return False
            return True if int(ip) >= 0 and int(ip) <= 255 else False
        
        def helper(s,ip):
            if s == "" and len(ip) == 4:
                res.append(".".join(ip))
                return 
            if len(ip) > 4:
                return 
            if not s:
                return 
            
            if check(s[:1]):
                helper(s[1:], ip + [s[:1]])
            if len(s) >= 2 and check(s[:2]):
                helper(s[2:], ip + [s[:2]])
            if len(s) >= 3 and check(s[:3]):
                helper(s[3:], ip + [s[:3]])
                
        helper(s,[])
        
        return res
            
            
                