# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []
        
                
        def get_depth(root):
            if not root:
                return 0
            return max(get_depth(root.left), get_depth(root.right)) + 1
        
        
        def print_tree(res,root,h,left,right):
            if not root:
                return 
            
            mid = (right - left) // 2 + left
            res[h][mid] = str(root.val)
            print_tree(res,root.left,h+1,left,mid-1)
            print_tree(res,root.right,h+1,mid+1,right)
            
        depth = get_depth(root)
        w = 2 ** depth - 1
        res = [[""]*w for i in range(depth)]
        print_tree(res,root,0,0,w-1)
        
        return res
            
        
        
            
        