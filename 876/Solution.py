# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        slow, quick = head, head
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            
        return slow