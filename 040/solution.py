class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        
        def helper(candidates, path, tmp_sum, pos):
            nonlocal res
            
            
            if tmp_sum == target:
                res.append(path[:])
            
            for i in range(pos, len(candidates)):
                if tmp_sum + candidates[i] > target:
                    break
                    
                if i != pos and candidates[i] == candidates[i-1]:
                    continue
                   
                
                tmp_sum += candidates[i]
                path.append(candidates[i])
                helper(candidates, path, tmp_sum, i+1)
                path.pop()
                tmp_sum -= candidates[i]
                
        
        helper(candidates, [], 0, 0)
        
        return res
                
        