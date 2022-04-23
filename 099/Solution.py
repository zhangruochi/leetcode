"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return 

        nodes = []

        def inorder(root):
            nonlocal nodes

            if not root:
                return 

            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)

        def traverse(root):
            nonlocal error_nodes
            if not root:
                return 

            if root.val == error_nodes[0]:
                root.val = error_nodes[1]
            elif root.val == error_nodes[1]:
                root.val = error_nodes[0]

            traverse(root.left)
            traverse(root.right)

        inorder(root)
        sorted_nodes = sorted(nodes)
        error_nodes = []

        for i, j in zip(nodes, sorted_nodes):
            if i != j:
                error_nodes.extend([i, j])
                break

        print(root)

        traverse(root)

