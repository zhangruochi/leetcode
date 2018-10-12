"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def depth(self,root):
        if not root:
            return 0
        else:
            return max(self.depth(root.left),self.depth(root.right))+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        O(nlogn)
        """
        if not root:
            return True
        else:
            return abs(self.depth(root.left)-self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution:
    def __height(self,root):
        if not root:
            return 0
        else:
            root.val = 1 + max(self.__height(root.left),self.__height(root.right))
            return root.val
        
    def __diff(self,left,right):
        if not left and not right:
            return 0
        elif not left and right:
            return right.val
        elif left and not right:
            return left.val
        else:
            return abs(left.val - right.val)            

    def __run(self,root):
        if not root:
            return True
        else:
            return self.__diff(root.left,root.right) <= 1 and self.__run(root.left) and self.__run(root.right) 

    def isBalanced(self,root):
        self.__height(root)
        return self.__run(root)        



                

            
            


                        



