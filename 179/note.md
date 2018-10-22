## 思路

- 自定义 merge_sort 的比较关系
- 哪个数字应该放在前面，可以将两个数字前后拼接在一起然后进行比较

```Python
    def compare(self,num1,num2):
        return True if num1+num2 >= num2+num1 else False

    def merge(self,list1,list2):
        result = []
        p1,p2 = 0,0
        while p1 < len(list1) and p2 < len(list2):
            if self.compare( list1[p1],list2[p2]):  # 比较关系用在此处
                result.append(list1[p1])
                p1 += 1
            else:
                result.append(list2[p2])
                p2 +=1
        result += list1[p1:]
        result += list2[p2:]
        
        return result
                
    
    def merge_sort(self,nums):
        if len(nums) <= 1:
            return nums

        length = len(nums)
        
        return self.merge(self.merge_sort(nums[:length//2]),self.merge_sort(nums[length//2:]))
```

# 使用 python 自带的函数 cmp_to_key
- cmp_to_key 接受一个 comparison function， negative number for less-than, zero for equality, or a positive number for greater-than

```Python
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str,nums))
        nums.sort(key = cmp_to_key(lambda x,y: int(x+y)-int(y+x)), reverse = True)
        return "".join(nums).lstrip("0") or "0"
```