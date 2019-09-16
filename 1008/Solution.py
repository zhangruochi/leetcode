# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return 
        
        def insert_node(root,val):
            if not root:
                return 
            
            if not root.left and root.val > val:
                root.left = TreeNode(val)
            if not root.right and root.val < val:
                root.right = TreeNode(val)
                
            if root.val > val:
                insert_node(root.left,val)
            else:
                insert_node(root.right,val)
        
        
        preorder = preorder[::-1]
        
        root = TreeNode(preorder.pop())
        
        while preorder:
            item = preorder.pop()
            insert_node(root,item)
        
        return root