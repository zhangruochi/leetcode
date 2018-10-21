## 思路
- 手写快排序
```Python
def quick_sort(self,nums,low, high):
        if low >= high:
            return 
        pivot = self.random_partition(nums,low,high)
        self.quick_sort(nums,low,pivot)
        self.quick_sort(nums,pivot+1,high)

    
    def random_partition(self,nums,low,high):
        index = randint(low,high)
        nums[index],nums[high] = nums[high],nums[index]
        i = low
        for j in range(low,high):
            if nums[j] < nums[high]:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        nums[i],nums[high] = nums[high],nums[i]
        return i
```



## 三指针
- 用一个指针标记从左往右数第一个不为0的位置
- 用一个指针标记从右往左数第一个不为2的位置
- 遍历一遍数组，当遇到该位置为2且 index < point_blue 时，交换两个位置的数字
- 当遇到该位置为0且 index > point_red 时，交换两个位置的数字
- 先交换2，因为交换回来的数字可能是0，还要再判断是否需要与前面不为0的位置交换
```Python

if nums[index] == 2 and index < point_blue:
    nums[index],nums[point_blue] = nums[point_blue],nums[index]
    point_blue -= 1
```