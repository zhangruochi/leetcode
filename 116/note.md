## 思路

- 自顶向下递归
- 同时递归左子树和右子树
- 如果做孩子和右孩子都存在，左孩子 -> 右孩子
- 如果左孩子的右孩子以及右孩子的左孩子都存在，左孩子的右孩子 -> 右孩子的左孩子
- 同时递归左孩子的左右孩子，右孩子的左右孩子，左孩子的右孩子和右孩子的左孩子
```Python
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
            
        def helper(left,right):
            if not left and not right:
                return 
            left.next = right       
            helper(left.left,left.right)
            helper(right.left,right.right)
            
            helper(left.right,right.left)

            
        if not root or (not root.left and not root.right):
            return 
    
        helper(root.left,root.right)
```