"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        res = []
        queue=deque()
        queue.append(root)

        num = 1

        while queue:
            count = num
            num = 0
            level_res = []
            while count:
                root = queue.popleft()
                level_res.append(root.val)

                if root.left:
                    queue.append(root.left)
                    num += 1
                
                if root.right:
                    queue.append(root.right)
                    num += 1

                count -= 1;

            res.append(level_res)

        return res