# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return None,None
        elif root.val <= V:
            res = self.splitBST(root.right,V)
            root.right = res[0]
            return root,res[1]
        else:
            res = self.splitBST(root.left,V)
            root.left = res[1]
            return res[0],root
            
        