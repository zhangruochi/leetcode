num=1, i=11, dp=[True, False, False, False, False, False, False, False, False, False, False, False]
num=1, i=10, dp=[True, False, False, False, False, False, False, False, False, False, False, False]
num=1, i=9, dp=[True, False, False, False, False, False, False, False, False, False, False, False]
num=1, i=8, dp=[True, False, False, False, False, False, False, False, False, False, False, False]
num=1, i=7, dp=[True, False, False, False, False, False, False, False, False, False, False, False]
num=1, i=6, dp=[True, False, False, False, False, False, False, False, False, False, False, False]
num=1, i=5, dp=[True, False, False, False, False, False, False, False, False, False, False, False]
num=1, i=4, dp=[True, False, False, False, False, False, False, False, False, False, False, False]
num=1, i=3, dp=[True, False, False, False, False, False, False, False, False, False, False, False]
num=1, i=2, dp=[True, False, False, False, False, False, False, False, False, False, False, False]
num=1, i=1, dp=[True, True, False, False, False, False, False, False, False, False, False, False]

num=5, i=11, dp=[True, True, False, False, False, False, False, False, False, False, False, False]
num=5, i=10, dp=[True, True, False, False, False, False, False, False, False, False, False, False]
num=5, i=9, dp=[True, True, False, False, False, False, False, False, False, False, False, False]
num=5, i=8, dp=[True, True, False, False, False, False, False, False, False, False, False, False]
num=5, i=7, dp=[True, True, False, False, False, False, False, False, False, False, False, False]
num=5, i=6, dp=[True, True, False, False, False, False, True, False, False, False, False, False]
num=5, i=5, dp=[True, True, False, False, False, True, True, False, False, False, False, False]

num=11, i=11, dp=[True, True, False, False, False, True, True, False, False, False, False, True]

num=5, i=11, dp=[True, True, False, False, False, True, True, False, False, False, False, True]
num=5, i=10, dp=[True, True, False, False, False, True, True, False, False, False, True, True]
num=5, i=9, dp=[True, True, False, False, False, True, True, False, False, False, True, True]
num=5, i=8, dp=[True, True, False, False, False, True, True, False, False, False, True, True]
num=5, i=7, dp=[True, True, False, False, False, True, True, False, False, False, True, True]
num=5, i=6, dp=[True, True, False, False, False, True, True, False, False, False, True, True]
num=5, i=5, dp=[True, True, False, False, False, True, True, False, False, False, True, True]


## TLE


```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        target = _sum // 2
        
        res = False
        
        
        
        def recursion(nums, cur_weight, depth, target):
            nonlocal res
            
            if depth == len(nums):
                return 
            
            if cur_weight >= target:
                if cur_weight == target:
                    res = True
                return 
            
            
            if(cur_weight + nums[depth] <= target):
                recursion(nums, cur_weight + nums[depth], depth+1, target)
            
            recursion(nums, cur_weight, depth+1, target)
        
        recursion(nums, 0, 0, target)
        
        return res
```