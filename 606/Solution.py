"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:

Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""

class Solution:

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        elif not t.left and not t.right:
            return "{}".format(t.val)
        elif t.left and not t.right:
            return "{}({})".format(t.val,self.tree2str(t.left))
        elif t.right and not t.left:
            return "{}()({})".format(t.val,self.tree2str(t.right))
        else:
            return "{}({})({})".format(t.val,self.tree2str(t.left),self.tree2str(t.right))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ""

        def pre_order(t):
            if not t:
                return ""
            elif not t.left and not t.right:
                return str(t.val)
            elif not t.right:
                return str(t.val) + "(" + pre_order(t.left) + ")"
            else:
                return str(t.val) + "(" + pre_order(t.left) + ")"  + "(" + pre_order(t.right) + ")"
            
        res = pre_order(t)
        return res

                
