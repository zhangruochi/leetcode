# Definition for a binary tree node.
# class TreeNode:
"""
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        values = []
        
        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        cum = 0
        for i in range(len(values)-1,-1,-1):
            cum += values[i] 
            values[i] = cum
            
        values = values[::-1]
        
        def inorder_change(root):
            if not root:
                return 
            
            inorder_change(root.left)
            root.val = values.pop()
            inorder_change(root.right)
            
        
        inorder_change(root)
        
        return root
        
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        tmp_sum = 0
        
        def inorder(root):
            nonlocal tmp_sum
            if not root:
                return 
            
            inorder(root.right)
            tmp_sum += root.val
            root.val = tmp_sum
            inorder(root.left)
            
        inorder(root)
        
        return root
        
            
            
            
            
            
                  
            
            
            
            