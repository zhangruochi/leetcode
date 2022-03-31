"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self,root,sum_,sum):
        if not root:
            return False
        sum_ += root.val   
        
        if not root.left and not root.right:
            return sum_ == sum
        
        return self.DFS(root.left,sum_,sum) or self.DFS(root.right,sum_,sum)
    
                
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        return self.DFS(root,0,sum)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root: return False
        
        res = False
        
        def traverse(root,sum_):
            
            nonlocal res
            
            if not root: return 
            
            if not root.left and not root.right:
                sum_ += root.val
                if sum_ == sum:
                    res = True
            
            traverse(root.left, sum_ + root.val)
            traverse(root.right, sum_ + root.val)
        
            
        traverse(root,0)
        return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        res = False

        def dfs(root, sum_):
            nonlocal res

            if not root:
                return 

            if not root.left and not root.right:
                if sum_ + root.val == targetSum:
                    res = True
            
            dfs(root.left, sum_ + root.val)
            dfs(root.right, sum_ + root.val)

        dfs(root, 0)

        return res
