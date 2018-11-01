## 思路

- 层次遍历，每一层放入一个list
- 遍历每层的list, 使得每个 node 指向它的下一个 node

```Python
from collections import deque
from collections import defaultdict

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        
        level = 0
        queue = deque([(root,level)])
        table = defaultdict(list)
        
        while queue:
            cur,level = queue.popleft()
            table[level].append(cur)
            if cur.left:
                queue.append((cur.left,level+1))
            if cur.right:
                queue.append((cur.right,level+1))
                
        for level,nodes in table.items():
            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]
```