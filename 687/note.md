## 思路

- 对于每个节点，假设左边最长路径已经知道，右边最长路径也已经知道，则：
```Python
left = maxpath(root.left)
right = maxpath(root.right)

left = left + 1 if root.left and root.left.val == root.val else 0
ååright = right + 1 if root.right and root.right.val == root.val else 0
```

- 此时，最长路径为：
```Python
longpath = max(longpath,left + right)
```

-  递归函数返回的是单边最长路径
```Python
return max(left,right)
```