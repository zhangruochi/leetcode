# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 1: 
            return [TreeNode(0)]
        res = []
        for l in range(1,N,2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res
        