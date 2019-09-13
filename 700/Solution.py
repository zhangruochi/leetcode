# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def traverse(root):
            if not root:
                return 
            elif root.val > val:
                return traverse(root.left)
            elif root.val < val:
                return traverse(root.right)
            else:
                return root
        return traverse(root)
                
        