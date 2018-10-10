"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

Both of the given trees will have between 1 and 100 nodes.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def root_recursion(self,root,list):
        if root == None:
            return 

        if (not root.left)  and (not root.right):
            list.append(root.val)

        self.root_recursion(root.left,list)
        self.root_recursion(root.right,list)

                

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list_root1 = []
        list_root2 = []
        
        self.root_recursion(root1,list_root1)
        print(list_root1)
        exit()
        self.root_recursion(root2,list_root2) 

        return list_root1 == list_root2

 
if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(5)  
    c = TreeNode(1)

    d = TreeNode(6)
    e = TreeNode(2)  
    f = TreeNode(9)

    g = TreeNode(8)
    h = TreeNode(7)
    i = TreeNode(4)


    a.left = b
    a.right = c

    b.left = d
    b.right = e

    e.left = h
    e.right = i

    c.left = f
    c.right = g

    print(Solution().leafSimilar(a,a))      











