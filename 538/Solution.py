"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        
        nodes = []
        
        def traverse(root,nodes):
            if not root:
                return 
            
            traverse(root.left,nodes)
            nodes.append(root)
            traverse(root.right,nodes)
        
        traverse(root,nodes)
        
        """
        for index,node in enumerate(nodes):
            node.val = sum( cur.val for cur in nodes[index:])
        """
        cum = 0
        for node in nodes[::-1]:
            node.val += cum
            cum = node.val
            
        return root




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        suffix_sum = []
        all_nodes = []
        
        def in_order(root):
            if not root:
                return 
            in_order(root.left)
            if suffix_sum:
                root.val += suffix_sum.pop()
            else:
                all_nodes.append(root.val)
            in_order(root.right)
        
        in_order(root)        
        cum = 0
        suffix_sum.append(0)
        for num in all_nodes[::-1][:-1]:
            cum += num
            suffix_sum.append(cum)
            
        in_order(root)
            
        return root
        
            
        
         
        