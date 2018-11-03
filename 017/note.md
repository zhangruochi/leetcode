##  思路

- 比较常见的递DFS和回溯的区别
    - 回溯是在解空间上不断前进和后退，如下面backtrack函数中的
    ```Python
    cur += c
    cur = cur[:-1]
    ```
    - 以下 dfs 把 cur 当做参数传递到最后一层，相当于对每一种情况都copy了一份解 


```Python
 def dfs(l,cur):
    if l == len(digits):
        ans.append(cur)
        return 
            
        for c in table[digits[l]]:
            dfs(l+1,cur+c)
        
def backtrack(l):
    nonlocal cur
    if l == len(digits):
        ans.append(cur)
        return 
            
    for c in table[digits[l]]:
        cur += c
        backtrack(l+1)
        cur = cur[:-1]
```


