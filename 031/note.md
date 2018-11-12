##  思路

- 比如“1，2，3”的全排列，依次是：
```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

所以题目的意思是，从上面的某一行重排到期下一行，如果已经是最后一行了，则重排成第一行。但是也不能根据给出的数组中的数字列出所有排列，因为要求不能占用额外的空间.

- example
```
6 5 4 8 7 5 1

从后面开始看，1和5调换了没有用。

7、5和1调换了也没有效果，因此而发现了8、7、5、1是递减的。

如果想要找到下一个排列，找到递增的位置是关键。

因为在这里才可以使其增长得更大。

于是找到了4，显而易见4过了是5而不是8或者7更不是1。

因此就需要找出比4大但在这些大数里面最小的值，并将其两者调换。

那么整个排列就成了：6 5 5 8 7 4 1

然而最后一步将后面的8 7 4 1做一个递增。
```



- 所以代码分为3大块
    - 从后往前，寻找第一个正序对的起始位置 i
    - 寻找 i 之后最小的大于 nums[i] 的数
    - 原地快排

```Python
from random import randint

class Solution:
    
    def partition(self,nums,left,right):
        pivot = random.randint(left,right)
        nums[pivot],nums[right] = nums[right],nums[pivot]
        
        i = left
        for j in range(left,right):
            if nums[j] < nums[right]:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        nums[right],nums[i] = nums[i],nums[right]
        return i
    
    
    def quick_sort(self,nums,left,right):
        if left >= right:
            return 
        pivot = self.partition(nums,left,right)
        self.quick_sort(nums,left,pivot-1)
        self.quick_sort(nums,pivot+1,right)

    
    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        flag = False
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                flag = True
                break
        
        if not flag:
            nums.reverse()
            return 
        
        
        min_ = float("inf")
        min_index = i
        for j in range(len(nums)-1,i,-1):
            if nums[j] > nums[i] and nums[j] < min_:
                min_ = nums[j]
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
        
        self.quick_sort(nums,i+1,len(nums)-1)
```

