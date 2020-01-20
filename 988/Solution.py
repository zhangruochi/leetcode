# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        ans = "{"
        
        def helper(root,tmp):
            nonlocal ans
            
            if not root:
                return 
            
            char = chr(ord('a') + root.val)
            tmp += char
            
            if not root.left and not root.right:
                
                if tmp[::-1] < ans:
                    ans = tmp[::-1]
            
    
            helper(root.left, tmp)
            helper(root.right, tmp)
        
        helper(root,"")
        
        return ans
        
        
        
        
            