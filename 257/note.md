## 思路

- 只有在到达叶子节点的时候才把路径添加到 paths 中
- 叶子节点只添加值，其余节点添加值和箭头

```python
def DFS(self,root,path,paths):
    if not root:
        return 

    if not root.left and not root.right:
        path += "{}".format(root.val)
        paths.append(path)
    path += "{}->".format(root.val)
        
    self.DFS(root.left,path,paths)
    self.DFS(root.right,path,paths)
            
    return paths
```