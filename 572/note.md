##  思路

- 如何判断两棵树完全相等？  可以采用先根遍历，isIdentical(s,t)= s.val==t.val AND isIdentical(s.left,t.left) AND isIdentical(s.right,t.right)
```Python
def DFS(self,s,t):
    if not s and not t:
        return True

    if not s or not t:
        return True

    return s.val == t.val and self.DFS(s.left,t.left) and self.DFS(s.right, t.right)
   
```

- 如何判断一棵树s含有另外一棵树t？

    - 可以采用广度优先搜索，以每个节点为根，求是否与t相等
    ```Python
    def isSubtree(self, s, t):
            """
            :type s: TreeNode
            :type t: TreeNode
            :rtype: bool
            """
            if not s:
                return 
            
            queue = deque([s])
            while queue:
                cur_node = queue.popleft()
                print(cur_node.val)
                if self.DFS(cur_node,t):
                    return True
                if cur_node.left: 
                    queue.append(cur_node.left)
                if cur_node.right:    
                    queue.append(cur_node.right)
            return False
    ```
    - 采用递归的方式,进行广度优先遍历
    ```Python
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        return  self.DFS(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    ```


"一棵子树上的点在深度优先搜索序列（即先序遍历）中是连续的。"