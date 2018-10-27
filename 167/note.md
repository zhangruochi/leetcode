## 思路

- two sum II 与 two sum 的不同之处在于 numbers 是有序的
- 设定两个指针，指向头和尾，根据两个指针处元素的和 sum 来改变两个指针的位置。
- 如果 sum > target 前移尾指针， sum < target 后移头指针