## 思路

```Python
class Solution:
      
    def diameterOfBinaryTree(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_depth(root):
            nonlocal diameter
            if not root:
                return 0

            left = max_depth(root.left)
            right = max_depth(root.right)

            diameter = max(diameter,left+right)

            return max(left,right) + 1 
    
        diameter = 0
        max_depth(root)
        
        return diameter

```

- 任意两点的最长路径
- 假设转折点在点node, 则路径为 =  左子树的最长长度 + 右子树的最长长度 + 2
- 如果转折点不在点node, 则node的值 = max(左子树的最长长度, 右子树的最长长度) + 1
- 在递归的过程中检测每个点作为转折点时的最长路径，同时返回它的单边最长路径