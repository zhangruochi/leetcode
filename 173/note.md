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