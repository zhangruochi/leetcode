## 思路

- 以任何一个结点为根，如果该 subtree 是 univalue subtree, 左子树要么不存在要么左子树的值等于根节点的值且右子树要么不存在要么右子树的值等于根节点的值
- 递归调用左右子树，如果该子树是 univalue subtree, 返回根节点的值代表整颗子树的值
- 如果某子树不是univalue subtree，则包含该子树的所有子树都不是 univalue subtree， 返回 ”#“

```Python
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            nonlocal count
            if not root: return     
            
            left = helper(root.left)
            right = helper(root.right)
            
            if (not left or left == root.val) and (not right or right == root.val):
                count += 1
                return root.val      
            return "#"
        count = 0
        helper(root)
        
        return count
```