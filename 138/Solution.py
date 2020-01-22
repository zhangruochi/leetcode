"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
""


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return 
        
        table = {}
        cur = head
        while cur:
            table[cur] = RandomListNode(cur.label)
            cur = cur.next
        
        cur = head
        while cur:
            table[cur].next = table.get(cur.next,None)
            table[cur].random = table.get(cur.random,None)
            cur = cur.next
        
        return table[head]



"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    
    def __init__(self):
        self.table = {}
        
    
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head: 
            return 
        
        if not head in self.table:
            self.table[head] = Node(head.val)
            self.table[head].next = self.copyRandomList(head.next)
            self.table[head].random = self.copyRandomList(head.random)
        
        return self.table[head]
            
