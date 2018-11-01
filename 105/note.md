## 思路

- 递归构建二叉树
- 根据preorder遍历的特点，preorder的第一个元素为根 root
- 根据中根遍历的特点，root 把 inorder 序列可分为左右子树
- 先构建左子树，再构建右子树，因为 preorder 先 popleft 出来的是左子树的根

```Python
class Solution:
    def recursive(self,preorder,inorder):
        if not inorder: return 
        index = inorder.index(preorder.pop())
        root = TreeNode(inorder[index])
        root.left = self.recursive(preorder,inorder[:index])
        root.right = self.recursive(preorder,inorder[index+1:])
        return root
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        preorder.reverse()
        return self.recursive(preorder,inorder)
    
```