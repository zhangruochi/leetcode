## Time Limit Exceeded

```python
class Solution:
    def minSwap(self, A: List[int], B: List[int]):
        res = float("inf")
        def helper(a,b,i,c):
            nonlocal res
            if i == len(a):
                res = min(res,c)
                return 

            if a[i] > a[i-1] and b[i] > b[i-1]:
                helper(a,b,i+1,c)

            if a[i] > b[i-1] and b[i] > a[i-1]:
                a[i],b[i] = b[i],a[i]
                helper(a,b,i+1,c+1)
                a[i],b[i] = b[i],a[i]

        helper(A,B,1,0)

        return res
```

## 思路

- keep[i]: 不交换位置i使得A[0...i]和B[0...i] 序列同时保持单调递增的最少交换次数
- swap[i]: 交换位置i使得A[0...i]和B[0...i] 序列同时保持单调递增的最少交换次数