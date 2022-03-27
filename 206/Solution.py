"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        tail = cur = head
        while cur.next:
            temp = cur.next.next
            cur.next.next = tail
            tail = cur.next
            cur.next = temp        
        return tail
            


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        tail,cur= head,head.next
        while cur:
            head.next = cur.next
            cur.next = tail
            tail = cur
            cur = head.next
        return tail


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return head

        cur = head
        tail = head

        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = tail
            tail = tmp
        
        return tail
        