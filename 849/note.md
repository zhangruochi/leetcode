## 思路
- 第一个距离为第一个人的距离减去0
- 中间的距离为两两之间的距离除2
- 最后一个距离为 len(A) - 1 - 最后一个人的位置
- 求以上所有距离的最大值




## itertools.groupby 操作结果

```python
for seat, group in itertools.groupby(seats):
            print(ans,list(group))

# [1,0,0,0,1,0,1]

# (0, [1])
# (0, [0, 0, 0])
# (0, [1])
# (0, [0])
# (0, [1])
```

