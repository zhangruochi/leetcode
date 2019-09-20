## 思路

- 遍历数组，先求 accumulative sum，保存在cum_sum里；
- cum_sum[0] = 0 是一个编程技巧。在求 subarray 的 sum 的时候，我们总是用 cum_sum[j] - cum_sum[i] 得到 nums[i+1:j]的 sum. 数组第一个元素也是一个单独的subarray，为了保持算法的逻辑的一致性，添加cum_sum[0] = 0 为前置。
- 遍历cum_sum，总是保存当前位置之前的最小值 pre_min，假设当前位置为 sum_,  则 sum_ - pre_min 为当前位置可得到的最大 subarray.