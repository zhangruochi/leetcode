## 思路
- 题目要求任何  sum(subarray) = k 的数量。
- 连接 prefix_sum,则任何 sum(subarray[i:j]) = prefix_sum[j] - prefix_sum[i-1], time complexity = O(1)
- 因为 prefix_sum[j] - prefix_sum[i] == k, 则: prefix_sum[j] - k = prefix_sum[i]
- 题目转化为,对于每一个 prefix_sum[j]，求前面有多少个 prefix_sum[i] = prefix_sum[j] - k
- 遍历 prefix_sum， 同时记录到当前位置为止，出现的 distinct value 的个数。

```Python
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
            
        table,count = {},0
        for prefix_j in prefix_sums:
            count += table.get(prefix_j-k,0)
            
            if not prefix_j in table:
                table[prefix_j] = 1
            else:
                table[prefix_j] += 1
            
        return count
```

- prefix_sum 可以不用提前计算

```Python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        table, count, cum = {0:1},0,0
        for num in nums:
            cum += num
            count += table.get(cum-k,0)
            table[cum] = table.get(cum,0)+1
        
        return count
```