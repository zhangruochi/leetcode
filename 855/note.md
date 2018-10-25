## 思路

- 用一个数组保存学生所坐的位置
- 遍历数组，找到两两之间最大的位置间隔，学生所坐的位置应该在最大的tmp_pos
```Python
tmp_dis = (cur - prev)//2
tmp_pos = prev + tmp_dis
```
- 使用二分搜索将学生位置插入数组
```Python
bisect.insort(list,student)
```

- 注意一开始的最大距离为list[0]
- 最后一个最大位置为
```Python
if self.N-1 - self.seated[-1] > max_dis:
    student = self.N-1
```