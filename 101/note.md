## 思路
- 首先对跟结点进行判断，如果为空，返回 True, 不为空，将左子树和右子树递归比较
```Python
 def mirror(self,left,right):
        if not left or not right:
            return left == right
        elif left.val != right.val:
            return False
        else:
            return self.mirror(left.left,right.right) and self.mirror(left.right,right.left)    
```
- 递归函数中, 出现左子树或右子树为空的情况,比较左子树和右子树(None == None 这种情况返回 True)
- 递归函数中, 左子树和右子树的值不相等，返回 False
- 左子树和右子树的值相等，则对左子树的左子树和右子树的右子树递归，对左子树的右子树和右子树的左子树递归
