## 思路

- 问题拆解：
    -  右子树不存在，H(root) = H(root.left) + 1
    -  左子树不存在，H(root) = H(root.right) + 1
    -  左右子树都存在, H(root) = min(H(root.left,root.right)) + 1

- 停止条件:
    -  节点为空，H(None) = 0

- 注意该题与求最大深度的区别
