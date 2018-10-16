## 思路
- 求 window size 为 3 的 moving avg
- 维持一个queue,  保留最近的三个数
- 注意边界条件，如果 window size  = 0, 所有输出为 0