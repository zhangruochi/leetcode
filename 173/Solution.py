"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.queue = deque()
        self.preorder(self.root)
        
    
    def preorder(self,root):
        if not root:
            return 
        self.preorder(root.left)
        self.queue.append(root.val)
        self.preorder(root.right)
        
        
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.queue else False
        

    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft()