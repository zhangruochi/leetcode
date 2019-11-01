# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        depth_hash = {}
        depth_hash[None] = 0
        
        def get_depth(root):
            nonlocal depth_hash    
            if not root:
                return 0
            l = get_depth(root.left)
            r = get_depth(root.right)
            depth_hash[root] = max(l,r) + 1
            return depth_hash[root] 
            
            
        def get_lca(root,depth_hash):

            if not root:
                return 
                        
            if depth_hash[root.left] == depth_hash[root.right]:
                return root
            elif depth_hash[root.left] > depth_hash[root.right]:
                return get_lca(root.left,depth_hash)
            else:
                return get_lca(root.right,depth_hash)
        
        get_depth(root)
        return get_lca(root,depth_hash)
        
                
                
            
            
            
            