##  思路
```Python
def DFS(self,root,sum_,sum):
        # 非叶子节点
        if not root:
            return False
        sum_ += root.val   
        
        # 到达叶子节点
        if not root.left and not root.right:
            return sum_ == sum
        
        return self.DFS(root.left,sum_,sum) or self.DFS(root.right,sum_,sum)
```


## 求所有路径的值

```Python
    def DFS(self,root,sum_,sums):
        if not root:
            return 
        sum_ += root.val   
        if not root.left and not root.right:
            sums.append(sum_)
        
        self.DFS(root.left,sum_,sums)
        self.DFS(root.right,sum_,sums)
```