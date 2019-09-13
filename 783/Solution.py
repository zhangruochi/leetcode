# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = None
        res = float("inf")
        def inorder(root):
            nonlocal prev,res
            if root:
                inorder(root.left)
                if prev == None:
                    prev = root.val
                else:
                    res = min(res,root.val - prev)
                    prev = root.val
                inorder(root.right)
        inorder(root)
        return res
        