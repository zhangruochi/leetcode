## 思路

- 矩阵转置的定义是 A[i][j] = A[j][i]
- 可以先创建一个空矩阵然后根据规律填充


## 最优思路
- 利用列表推导，根据列元素来填充行元素
```Python
def transpose(self, A):
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
```
