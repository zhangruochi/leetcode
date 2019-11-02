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


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        if not nums:
            return res
        
        def helper(nums,item, visited):
            if len(item) == len(nums):
                res.append(item[:])
                return 
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    item.append(num)
                    helper(nums,item, visited)
                    item.pop()
                    visited.remove(num)
                    
        helper(nums,[],set())
        return res
                                


if __name__ == '__main__':
    solution = Solution()
    for item in solution.permute([1,2,3,4]):
        print(item)