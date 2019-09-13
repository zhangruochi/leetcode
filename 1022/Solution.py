# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        numbers = []
        def traverse(root,num):
            nonlocal numbers 
            if not root:
                return 
            
            if not root.left and not root.right:
                numbers.append(num + str(root.val))
                return 
            
            traverse(root.left,num + str(root.val))
            traverse(root.right,num + str(root.val))
            
        def func(num):
            return int(num,2)
        
        traverse(root,"")
        
        return sum(list(map(func,numbers)))
        