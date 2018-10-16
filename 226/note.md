## 思路
- 问题拆解
- 针对当前根节点，需要交换左右子结点
- 对于所有子节点，也需要交换各自的左右子节点
```Python
root.left,root.right = root.right,root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
```

- 深度优先遍历和广度优先遍历都适用