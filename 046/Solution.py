from itertools import permutations
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """      
        
        res,ans = [],[]
        if not nums:
            return res

        def dfs(ans):
            if len(ans) == len(nums):
                res.append(list(ans))
                return 
            
            for item in nums:
                if item not in ans:
                    ans.append(item)
                    dfs(ans)
                    ans.pop()
        
        dfs(ans)
        return res
                    
from itertools import permutations
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """       
        return list(permutations(nums,len(nums)))


if __name__ == '__main__':
    solution = Solution()
    for item in solution.permute([1,2,3,4]):
        print(item)