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