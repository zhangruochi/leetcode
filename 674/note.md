## 思路

- 用一个变量prev保存前一个数字，用 count 保存当前递增序列的长度，用 max_ 变量维持当前的最大值
- 遍历当前数组
- 如果 nums[i] > prev
    - count 增加，更新 max_
    - 更新  prev = nums[i]
- 如果  nums[i] < prev
    -  count = 1（**注意此处为1**）

- 最终的 max_为结果