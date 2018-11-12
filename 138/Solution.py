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
            
