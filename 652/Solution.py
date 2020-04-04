"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        res = []
        str_map = defaultdict(int)
        
        def inorder(root, string):
            if not root:
                return "#"
            
            new_string = inorder(root.left, string) + inorder(root.right, string) +  str(root.val)
            
            if str_map[new_string] == 1:
                res.append(root)
            
            str_map[new_string] += 1
                
            return new_string
        
        inorder(root, "")
        
        return res
            
            
            
            
            
            
            
            
        
        