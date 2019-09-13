"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self,root,path,paths):
        if not root:
            return 

        if not root.left and not root.right:
            path += "{}".format(root.val)
            paths.append(path)
        path += "{}->".format(root.val)
        
        self.DFS(root.left,path,paths)
        self.DFS(root.right,path,paths)
            
        return paths
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """    
        if not root:
            return []
        return self.DFS(root,"",[])



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if not root: return ""
        
        res = []
        
        def traverse(root,path):
            nonlocal res
            if not root:
                return 
            
            if not root.left and not root.right:
                res.append(path + str(root.val))
            
            traverse(root.left,path + str(root.val) + "->")
            traverse(root.right, path + str(root.val) + "->")
        
        traverse(root,"")
        
        return res
        
