"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000

 

注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        
        index_map = {num: i for i, num in enumerate(inorder)}

        def reconstruct(l,r):
            nonlocal inorder,preorder,index_map

            if l >= r:
                return None

            index = index_map[preorder.pop()]
            root = TreeNode(inorder[index])
            
            root.left = reconstruct(l,index)
            root.right = reconstruct(index+1,r)

            return root

        if not preorder or not inorder:
            return None        

        preorder.reverse()
        return reconstruct(0,len(preorder))
