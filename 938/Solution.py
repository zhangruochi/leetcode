# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        def traverse(root):
            nonlocal res
            if not root:
                return 
            else:
                if root.val < L:
                    traverse(root.right)
                elif root.val > R:
                    traverse(root.left)
                else:
                    res += root.val
                    traverse(root.left)
                    traverse(root.right)
                    
        traverse(root)
        return res