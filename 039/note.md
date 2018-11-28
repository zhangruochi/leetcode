## 思路

- backtracking 是，用level变量保存当前位置，为了防止重复计算，遍历的起始位置都是当前位置
- 递归出口是当 tmp 中元素的和已经大于target.
- 将 tmp 保存到结果中时要复制一份

```Python
        def rec(level,tmp):
            if sum(tmp) > target:
                return
            elif sum(tmp) == target:
                ans.append(list(tmp))
            
            for i in range(level,len(candidates)):
                tmp.append(candidates[i])
                rec(i,tmp)
                tmp.pop()
```