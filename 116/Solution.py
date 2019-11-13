"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
            
        def helper(left,right):
            if not left and not right:
                return 
            left.next = right       
            helper(left.left,left.right)
            helper(right.left,right.right)
            
            helper(left.right,right.left)

            
        if not root or (not root.left and not root.right):
            return 
    
        helper(root.left,root.right)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return 
        
        res = root
        prev = None
        level = 0
        queue = deque([(root,level)])
        visited = set()
        
        while queue :
            root,level = queue.popleft()
            
            if level not in visited:
                visited.add(level)
                prev = root
            else:
                root.next = prev
                prev = root
                
            if root.right:
                queue.append((root.right,level+1))
            if root.left:
                queue.append((root.left,level+1))
                
        return res
        