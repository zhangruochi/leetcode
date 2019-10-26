class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        def helper(i,pos,num):
            if pos == len(nums):
                return 
            
            for i in range(pos, len(nums)):
                if i != pos and nums[i-1] == nums[i]:
                    continue
                num.append(nums[i])
                res.append(num[:])
                helper(pos,i+1,num)
                num.pop()
        
        helper(0, 0, [])
        res.append([])
        
        return res
        