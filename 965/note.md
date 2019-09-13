## 思路

- 采用Top-down 的recursion 方法
- 对于每一个节点，返回 True 的条件是:
    - 把root和左子树看成 left
    - 把root和右子树看成 right
    - left == right
- 以 left 为例，left 的值为：
    - root.left 不存在
    - root.left 存在且 root.left.val == root.val 
- 递推公式是：
isUnivalTree(root) = left and right and isUnivalTree(root.left) and isUnivalTree(root.right)


