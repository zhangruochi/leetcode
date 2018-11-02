## 思路

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
- 可以看到，最后形成的链表是 preorder 
- 把 preorder 的顺序倒过来，先遍历右子树，再遍历左子树. 
- 用一个 prev 变量保存上一次递归的结果，并把上一次递归的结果保存在当前根节点的右子树，左子树置为None