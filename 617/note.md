## 思路

```Python
def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val = t1.val + t2.val
        
        if not t1:
            return t2
        
        if not t2:
            return t1
        
        
        
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1
        
```

- 只考虑当前结点，有三种情况
    - 左右子树都存在，值相加
    - 左不存在，等于右子树
    - 右不存在，等于左子树

- 当前结点的左子树的值等于递归调用两棵左子树的值
- 当前结点的右子树的值等于递归调用两棵右子树的值

