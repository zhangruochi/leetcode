"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        all_nodes = []
        for head in lists:
            while head:
                all_nodes.append(head)
                head = head.next
        all_nodes.sort(key = lambda x:x.val)
        for i in range(len(all_nodes)-1):
            all_nodes[i].next = all_nodes[i+1]
        
        if all_nodes:
            return all_nodes[0]
        
        return []