"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.mirror(root.left,root.right)

    def mirror(self,left,right):
        if not left or not right:
            return left == right
        elif left.val != right.val:
            return False
        else:
            return self.mirror(left.left,right.right) and self.mirror(left.right,right.left)    


                
                   
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(left, right):
            
    if not left and not right:
        return True

    if not left and right:
        return False

    if not right and left:
        return False 

    if left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left):
        return True
    else:
        return False

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True        
            
        return helper(root.left, root.right)
         
        


if __name__ == '__main__':
    a = TreeNode(1)
    """
    b = TreeNode(2)
    a.left = b
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(4)
    g = TreeNode(3)
    """
    print(Solution().isSymmetric(a))

        
