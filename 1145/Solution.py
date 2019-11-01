# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        
        def find_x(root,x):
            if not root:
                return False
            
            if root.val == x:
                return root
        
            res = find_x(root.left,x)
            
            if not res:
                return find_x(root.right,x)
            
            return res
        

        def count_tree(root):
            if not root:
                return [0,0,0]
            l,_,_ = count_tree(root.left) 
            r,_,_ = count_tree(root.right)
            return [l + r + 1,l,r]
        
        
        x_root = find_x(root,x)
        m,l,r = count_tree(x_root)
        
        return True if max(n-m,l,r) > n // 2 else False
        
        
        
        
        
        
        