##自己的思路   time complexity = O(n)   space complexity = 0(1)
先判断是否是单调增，在不是单调增的情况下是否是单调减。如果都不是，就返回 False.


##最优思路
单调增和单调减不可能同时出现, 一次遍历，如果数组中出现了 nums[i] > nums[i+1] 又出现了 nums[i] < nums[i+1] 的情况，则不为单调数组