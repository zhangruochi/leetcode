"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

# Definition for a binary tree node.

from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 

        root.left,root.right = root.right,root.left

        self.invertTree(root.left)
        self.invertTree(root.right)


        return root

    def ivertTree2(self,root):
        """BFS
        """
        if not root:
            return None
        queue = deque()
        queue.add(root)

        while queue:
            node = queue.popleft()
            node.left,node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


    def invertTree3(self,root):
        """DFS
        """
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()
            node.left,node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root























