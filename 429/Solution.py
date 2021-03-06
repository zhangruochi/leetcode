"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
 

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
from collections import defaultdict
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        level = 0
        queue,result = deque([(root,level)]),defaultdict(list)

        while queue:
            cur,level = queue.popleft()
            result[level].append(cur.val)
            for child in cur.children:
                queue.append((child,level+1))
        return [result[i] for i in range(len(result))]
            

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
from collections import defaultdict
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root: return 
        
        level = 0
        table = defaultdict(list)
        
        queue = deque([(level,root)])
        while queue:
            level,root = queue.popleft()
            table[level].append(root.val)
            
            for child in root.children:
                queue.append((level+1,child))
        
        
        return [table[i] for i in range(len(table))]
            
        
        
        
        
