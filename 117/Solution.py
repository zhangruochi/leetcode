"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
"""

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
                
            