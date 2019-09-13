"""
Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
       

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return []
        
        new_tree = []
        def inorder(node,new_tree):
            if not node:
                return 
            inorder(node.left,new_tree)
            new_tree.extend([node.val,None])
            inorder(node.right,new_tree)
        
        inorder(root,new_tree)    
        new_tree.pop() 
        
        return new_tree
            


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def in_order(root):
            if root:
                yield from in_order(root.left)
                yield root
                yield from in_order(root.right)
        
        gen = in_order(root)
        ans = prev = next(gen)
        for node in gen:
            prev.right = node
            prev = node
        
        prev.right = None
        
        # while ans:
        #     print(ans.val)
        #     ans = ans.right
        
        return ans
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        dummy = cur = TreeNode(None)
        
        def in_order(root):
            nonlocal cur
            if root:
                in_order(root.left)
                root.left = None
                cur.right = root
                cur = cur.right
                in_order(root.right)
        
        in_order(root)
        return dummy.right
        