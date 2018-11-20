## 思路

- 每个结点都要搜索sum, 递归式为:
```Python
self.find_path(root,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right,sum)
```

- 从每个结点开始搜索sum, 找出该条路径里所有 sum 等于target的 path
```Python
return int(root.val == target) + self.find_path(root.left,target - root.val) + self.find_path(root.right, target - root.val)
```