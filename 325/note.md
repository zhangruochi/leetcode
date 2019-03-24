## 思路
- sum of subarray
    **prefix_sum[j] - prefix[i] = k**

- 遍历数组，用 table 保存 prefix_sum，key 为 prefix_sum，vlaue 为 index
- 更新 table 的规则，如果 table 中已有该 prefix_sum, 则跳过不更新，因为我们只想保留索引最小的位置，以便获得最长的subarray
- 如果当前 prefix_sum == k, 则最长子数组为当前的索引
- 如果当前 prefix_sum != k, 查看 table 中是否存在prefix_sum[j] - k,如果存在， 用 j-i 更新 length


```Python
class Solution:
    
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        table,cum,length = {},0,0
        for j,num in enumerate(nums):
            cum += num
            if cum == k:
                length = j+1
            else:
                if cum-k in table:
                    length = max(length,j - table.get(cum-k))
        
            if not cum in table:
                table[cum] = j
                
        return length
```


