## 思路 
- 将num2复制到num1后面
- 对num1进行插入排序，从m位置开始
- 时间复杂度为O(n^2)

```Python
class Solution:
    def insert_sort(self,lists,m,n):
        for i in range(m,m+n):
            tmp = lists[i]
            j = i-1
            while j >= 0:
                if tmp < lists[j]:
                    lists[j+1] = lists[j]
                    j -= 1
                else:
                    break
            lists[j+1] = tmp
```


## 最优思路
- 用一个指针p1保存num1尾部，p2保存num2尾部, p_merge保存合并数组的尾部
- 三个指针从尾部往前移动
```Python
def merge(self, nums1, m, nums2, n):

        p1,p2,p_merge = m - 1, n - 1, m + n - 1

        while p1>= 0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[p_merge] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_merge] = nums2[p2]
                p2 -= 1
            p_merge -= 1        

        if p2 >= 0:
            nums1[:p_merge+1] = nums2[:p2+1] 
```