"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(range(1,n+1), k)



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:        
        def recurse(arrays, depth, pos, path, res):
            if depth == k:
                res.append(path[:])
                return 
            
            for i in range(pos, n):
                path.append(arrays[i])
                recurse(arrays, depth+1, i+1, path, res)
                path.pop()
        
            return res
        
        return recurse(list(range(1,n+1)), 0, 0, [], [])
    
            
                