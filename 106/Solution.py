"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return 
        
        index = inorder.index(postorder.pop())
        root = TreeNode(inorder[index])
        root.right = self.buildTree(inorder[index+1:],postorder)
        root.left = self.buildTree(inorder[:index],postorder)
        
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return None
       
        def helper(left_index,right_index):
            if left_index > right_index:
                return 
            
            root = TreeNode(postorder.pop())
            mid = id_index[root.val]
            
            root.right = helper(mid+1,right_index)
            root.left = helper(left_index,mid-1)
            
            return root
        
        id_index = {num:index for index,num in enumerate(inorder)}
       
        
        return helper(0,len(inorder)-1)