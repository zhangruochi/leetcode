## 思路

- 先用先根遍历遍历BST，得到从小到大的排序，存在 queue 中
- 然后next就是不断出队元素

## space complexity 为O(h)
- 创建一个迭代器，迭代器中用 stack 存储左子树递归到叶子节点。
- 每次next就每次yeild 栈顶元素，如果出栈元素存在右子树，此时将右子树全部入栈

```Python
from collections import deque

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        if not self.root:
            self.flag = False  
        else:
            self.flag = True
        self.iter = iter(self)
        
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.flag
        
            

    def __iter__(self):
        root = self.root
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            cur = stack.pop()
            if cur.right:
                root = cur.right
            if not root and not stack:
                self.flag = False                
            yield cur.val

        
    
    def next(self):
        """
        :rtype: int
        """
        return next(self.iter)
```       

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.items = []
        def in_order(root):
            if not root:
                return 
            else:
                in_order(root.left)
                self.items.append(root)
                in_order(root.right)
        in_order(root)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.items.pop(0).val
        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.items else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```