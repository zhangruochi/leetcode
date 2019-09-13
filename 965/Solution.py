# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        return (not root.left or root.val == root.left.val) and (not root.right or root.val == root.right.val) and self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
                