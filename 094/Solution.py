"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""
class Solution:
    # 递归版本
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def inorder(root):
            nonlocal result
            if not root:
                return     
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        return result

    # 迭代版本

    def inorderTraversal(self, root):
        if not root:
            return []
        stack = []
        result = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            cur_node = stack.pop()
            result.append(cur_node.val)
            root = cur_node.right
        return result    



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        def helper(root):
            if not root:
                return 
            
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)

        return res












