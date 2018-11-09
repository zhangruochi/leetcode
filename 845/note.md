## 思路
- 遍历数组，保存当前元素之前有多少个元素小于这个元素和当前元素之后有多少个元素大于这个元素

```Python
## 求当前元素之前有多少个元素小于这个元素
if A[left] > A[left-1]:
    dp1.append(dp1[-1]+1)
else:
    dp1.append(0)
                
## 求当前元素之后有多少个元素大于这个元素
if A[right] > A[right+1]:
    dp2.append(dp2[-1]+1)
else:
    dp2.append(0)
            
left += 1
right -= 1
```

- mountain subarray 的长度为dp1+dp2对应的元素，但是当任意位置为0时，元素为0