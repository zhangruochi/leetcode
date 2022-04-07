"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        res = False

        if not B:
            return res

        def helper(A,B):
            
            if not B:
                return True
            
            if not A or A.val != B.val:
                return False
            
            return helper(A.left,B.left) and helper(A.right, B.right)


        def pre_order(A,B):
            nonlocal res

            if not A:
                return 
            
            if A.val == B.val:
                if helper(A,B):
                    res = True


            pre_order(A.left, B)
            pre_order(A.right, B)

            return False

        pre_order(A,B)

        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def is_same(root_a, root_b):
    if not root_a and not root_b:
        return True
    elif not root_b and root_a:
        return True
    elif not root_a and root_b:
        return False
    else:
        return root_a.val == root_b.val and is_same(root_a.left, root_b.left) and is_same(root_a.right, root_b.right)
                
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        if not A or not B:
            return False
        else:
            return is_same(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B) 
            