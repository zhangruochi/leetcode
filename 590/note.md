"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def travserse(root):
            if not root:
                return 
            else:
                for child in root.children:
                    travserse(child)
                res.append(root.val)
            
            return res
        
        return travserse(root)
        
        