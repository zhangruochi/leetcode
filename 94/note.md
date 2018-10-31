## 思路

- root左子树不为空时，不断入栈左子树 rot = root.left
- 为空时，弹出栈顶元素cur，记录下当前节点的值，同时 root = cur.right, 再重复第一步