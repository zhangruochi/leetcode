## 思路
- 对每颗树开辟一个数组，将数组递归进去，遇到叶节点就加入到数组里
```Python
def root_recursion(self,root,list):
        if root == None:
            return 

        if (not root.left)  and (not root.right):
            list.append(root.val)

        self.root_recursion(root.left,list)
        self.root_recursion(root.right,list)
```
- 如果结点是空，则返回
- 如果结点的左右子树都为空，则说明为叶结点，加入到数组，再对左右字数分别递归
