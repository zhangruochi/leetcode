## 思路

- 采用内置的 combinations 函数，求不同长度的combination组合
- backtract, 
```Python
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
            
            # 进入左子树
            dfs(i+1)
            indexs[i] = 0
            # 进入右子树
            dfs(i+1)
        
        dfs(0)
        return ans
```