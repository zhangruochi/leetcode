"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def traverse(root,depth):
            if not root:
                return depth
            
            if not root.left and not root.right:
                return depth + 1
            
            return max(traverse(root.left, depth+1),traverse(root.right, depth + 1))
        
        return traverse(root,0)
        
            
            



class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)

## top_down 
class Solution(object):
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def top_down(root,level):
            nonlocal result
            if not root:
                return 
            if not root.left and not root.right:
                result = max(result,level)

            top_down(root.left,level+1)
            top_down(root.right,level+1)

## bottom_up 
class Solution(object):
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    b.right = c

    print(Solution().maxDepth(a))

        

                    