#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com

"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

"""
解题思路：

假设两棵树的根节点分别是p和q。

如果p和q是同一个节点，那么它们必然相同。
如果p和q不是同一个节点，但是其中有一个为空，那么它们必然不同。
如果p和q不是同一个节点，并且都不为空，继续处理：
如果p和q所含的值相同，那么就递归比较p和q的左右子树。
如果p和q所含的值不同，那么这两棵树就不同了。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True

        elif p == None or q == None:
            return False

        else:
            return  p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


             
                
