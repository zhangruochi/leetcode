"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

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
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import deque
from collections import defaultdict
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        res = defaultdict(list); level = 0
        queue=deque()
        queue.append((root,level))

    
        while queue:

            root,level = queue.popleft()
            res[level].append(root.val)

            if root.left:
                queue.append((root.left,level + 1))
            if root.right:
                queue.append((root.right, level + 1))
    

        return [res[i] if i% 2 ==0 else res[i][::-1] for i in range(len(res))]