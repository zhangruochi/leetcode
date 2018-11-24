## 思路

-  从左到右遍历数组，得到当前位置 i 之前所有元素的和, prefix_sum_left
-  从右到左遍历数组，得到当前位置 i 之前所有元素的和, prefix_sum_right
-  比较 prefix_sum_left 和 prefix_sum_right， 返回第一个相等的位置，否则返回 1