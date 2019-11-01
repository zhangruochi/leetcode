class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
                
        def helper(accounts,flag):
            res = {}
            visited = {}
            
            if flag:
                return accounts
            
            flag = True
            indx = 0
            for account in accounts:
                for email in account[1:]:
                    if email in visited:
                        res[visited[email]].extend(account[1:])
                        flag = False
                        break
                else:
                    for email in account[1:]:
                        visited[email] = indx
                    res[indx] = account
                    indx += 1

            return helper(res.values(),flag)
    
    
        def sorted_func(item):
            return [item[0]] + sorted(set(item[1:]))
        
        return  list(map(sorted_func,helper(accounts,False)))  
            
        