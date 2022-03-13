"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidatesmay only be used once in the combination.

Note:The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
Constraints:

1 <=andidates.length <= 100
1 <=andidates[i] <= 50
1 <= target <= 30
"""


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
                
        