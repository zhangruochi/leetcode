"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def rec(level,tmp):
            if sum(tmp) > target:
                return
            elif sum(tmp) == target:
                ans.append(list(tmp))
            
            for i in range(level,len(candidates)):
                tmp.append(candidates[i])
                rec(i,tmp)
                tmp.pop()
        
        rec(0,[])
        return ans

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def helper(candidates, pos, path, temp_sum):
            nonlocal res
            if temp_sum == target:
                res.append(path[:])
    
            for i in range(pos, len(candidates)):
                if temp_sum + candidates[i] > target:
                    break
                path.append(candidates[i])
                helper(candidates, i,  path, temp_sum+candidates[i])
                path.pop()
                
 
                    
        helper(candidates, 0, [], 0)
        
        return res

        
            