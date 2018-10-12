## 自己的思路  Time Complexity O(nlogn)   

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

- 需要对二叉树的每个节点都进行判断是否平衡
- 问题拆解,根节点是否平衡取决于左子树与右子树是否平衡以及左子树与右子树的高度差是否小于等于1
```Python
abs(self.depth(root.left)-self.depth(root.right)) <= 1 and 
self.isBalanced(root.left) and 
self.isBalanced(root.right)
```
- 停止条件是,如果节点为空，是平衡的
```Python
if not root:
    return True
```


## 最优思路 Time Complexity O(logn)

- 上述思路在计算每个节点的高度时都要递归计算, 重复计算量很多
- 可以用height函数先给每个节点计算高度,保存在val变量中
```Python
def __height(self,root):
        if not root:
            return 0
        else:
            root.val = 1 + max(self.__height(root.left),self.__height(root.right))
            return root.val
```
- 在计算是否平衡时直接读取树的高度
```Python
def __run(self,root):
        if not root:
            return True
        else:
            return self.__diff(root.left,root.right) <= 1 and self.__run(root.left) and self.__run(root.right) 
```

