"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = quick = dummy
        while quick:
            if n >= 0:
                n -= 1
                quick = quick.next
            else:
                quick = quick.next
                slow = slow.next
        slow.next = slow.next.next
        return dummy.next
            

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        count, p = 0, dummy
        while p:
            count += 1
            p = p.next
        k = count - n - 1
        
        p = dummy
        while k:
            p = p.next
            k -= 1
            
        p.next = p.next.next
        return dummy.next
            
        
    
        