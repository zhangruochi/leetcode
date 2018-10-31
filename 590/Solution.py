"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def recursive(self,root,lists):
        if not root: return 
        for child in root.children:
            self.recursive(child,lists)
        lists.append(root.val)
    
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        lists = []
        self.recursive(root,lists)
        return lists