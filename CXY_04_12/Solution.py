"""
给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

3
解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]
提示：

节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paths-with-sum-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        res = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def helper(root, sum_, prefix_sum):
            
            nonlocal res

            if not root:
                return 0

            sum_ += root.val

            if  prefix_sum.get(sum_ - sum, 0) > 0:
                res += prefix_sum[sum_ - sum]
            
            prefix_sum[sum_] += 1

            helper(root.left,sum_, prefix_sum)
            helper(root.right,sum_, prefix_sum)

            prefix_sum[sum_] -= 1

        helper(root, 0, prefix_sum)

        return res

