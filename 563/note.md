## 思路

- 先根遍历求所有结点的和
```Python
def preorder(self,node):
        if not node:
            return 0
        return node.val + self.preorder(node.left) + self.preorder(node.right)
```

- 计算某个结点的tilt
```Python
def tilt_node(self,node):
        if not node:
            return 0
        return abs(self.preorder(node.left) - self.preorder(node.right))
```

- 计算所有结点的 tilt 和
```Python
def findTilt(self, root):
    if not root:
        return 0        
    return self.tilt_node(root) + self.findTilt(root.left) + self.findTilt(root.right)
```


## 最优思路
- _sum(root) 为以root为根的子树的结点的和
-  某棵树的结点的和又等于左子树的和加右子树的和加上结点值，
-  自下往上思考，每次在求左右子树的和的时候，可以顺便计算左右子树的差

```Python
class Solution:
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = 0
        def _sum(root):
            nonlocal total
            if not root: return 0
            left,right = _sum(root.left), _sum(root.right)
            total += abs(left-right)
            return root.val + left + right
        _sum(root)
        return total
```

