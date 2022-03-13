from itertools import permutations
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(set(list(permutations(nums))))

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        
        nums.sort()
    
        def helper(item,visited):
            if len(item) == len(nums):
                res.append(item[:])
                return 
            
            for i,num in enumerate(nums):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                

                item.append(nums[i])
                visited[i] = True
                helper(item,visited)
                item.pop()
                visited[i] = False
        
        res = []  
        item = []
        visited = [False] * len(nums)
        helper(item,visited)
        
        return res



class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    
        def helper(path, visited):

            if len(path) == len(nums):
                res.append(path[:])
            
            for i in range(len(nums)):

                if visited[i] or ( i > 0 and nums[i] == nums[i-1] and visited[i-1] ):
                    continue


                path.append(nums[i])
                visited[i] = True
                helper(path, visited)

                # backtrack
                visited[i] = False
                path.pop()
        
        res = []
        visited = [False] * len(nums)
        nums.sort()
        helper([], visited)

        return res