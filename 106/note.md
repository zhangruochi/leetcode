## 思路

- 递归构建二叉树
- 根据后根遍历的特点，postorder的最后一个元素为根 root
- 根据中根遍历的特点，root 把 inorder 序列可分为左右子树
- 先构建右子树，再构建左子树，因为 postorder 先 pop 出来的是右子树的根

```Python
class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return 
        
        index = inorder.index(postorder.pop())
        root = TreeNode(inorder[index])
        root.right = self.buildTree(inorder[index+1:],postorder)
        root.left = self.buildTree(inorder[:index],postorder)
        
        return root
```