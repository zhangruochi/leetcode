"""
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return []
        
        nodes = []
        
        def inorder(root):
            nonlocal nodes
            if not root:
                return 
            
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)
            
        def construct(nodes):
            
            if not nodes:
                return None
                
            
            m_idx = len(nodes) // 2
            root = nodes[m_idx]
            
            root.left = construct(nodes[:m_idx])
            root.right = construct(nodes[m_idx+1 :])
            
            return root
            
            
        inorder(root)
        
        return construct(nodes)
        
        
        
        