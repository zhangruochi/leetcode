class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        indexs = [0]*len(nums)
        
        def dfs(i):
            if i >= len(nums):
                return 
            indexs[i] = 1        
            ans.append([nums[i] for i in range(len(indexs)) if indexs[i] == 1])
    
            dfs(i+1)
            indexs[i] = 0
            dfs(i+1)
        
        dfs(0)
        return ans

from itertools import combinations
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(0,len(nums)+1):
            ans.extend(list(combinations(nums,i)))
        return ans
            
            