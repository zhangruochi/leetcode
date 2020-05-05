"""
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def get_level(root, level):
            nonlocal max_level

            if not root:
                max_level = max(max_level, level)
                return 

            get_level(root.left, level + 1)
            get_level(root.right, level + 1)

        def level_order(root):
            queue = deque()
            queue.append((root,0))

            res = []

            while queue:
                root, level = queue.popleft()
                if root:
                    res.append(root.val)
                else:
                    res.append(root)

                if root and level < max_level-1:
                    queue.append((root.left, level + 1))
                    queue.append((root.right, level + 1))
        
            return res


        max_level = 0
        get_level(root, 0)
        res = level_order(root)

        return "#".join(map(str,res))
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "None":
            return 

        data_array = []
        for num in data.split("#")[::-1]:
            if num == "None":
                data_array.append(None)
            else:
                data_array.append(int(num))


        # print(data_array)

        queue = deque()
        head = TreeNode(data_array.pop())
        queue.append(head)
        
        while queue:
            root = queue.popleft()

            if data_array:
                left = data_array.pop()
                if left != None:
                    left = TreeNode(left)
                    queue.append(left)
                root.left = left

            if data_array:
                right = data_array.pop()
                if right != None:
                    right = TreeNode(right)
                    queue.append(right)
                root.right = right
            
        
        return head

            







        
        

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))