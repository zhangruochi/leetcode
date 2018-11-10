## 思路

- 题目中说 Rotated Sorted Array，其实也有单调递增的情况。
- 先判断 nums[-1] 和 nums[0] 的大小，如果 nums[-1] > nums[0], 直接返回 nums[0]
- 如果存在 rotated， 可以用二分查找找出转折点
    ```Python
        while low <= high:
            mid = low + ((high-low)>>1)

            # 停止条件
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            # 这半条件
            if nums[mid] >= nums[low]:
                low = mid + 1
            elif nums[mid] <= nums[high]:
                    high = mid - 1
```