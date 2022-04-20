"""
Given the head of a linked list, rotate the list to the right by k places.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        cur = head 
        count = 0
        while cur:
            count += 1
            cur = cur.next 

        k = k % count
        n = count - k - 1

        cur = head 
        while n :
            cur = cur.next 
            n -= 1

        if not cur.next:
            return head

        new_head = tail = cur.next
        cur.next = None 

        while tail.next:
            tail = tail.next 
        tail.next = head 

        return new_head 





            
            
