"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result,stack,last_visited = [],[],None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            cur = stack[-1]
            if (not cur.right) or cur.right == last_visited:
                last_visited = stack.pop()
                result.append(cur.val)
            elif cur.right:
                root = cur.right
                
        return result