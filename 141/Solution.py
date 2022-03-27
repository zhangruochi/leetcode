"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow,quick = head,head
        while slow and quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False
            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        q = s = head
        flag = False

        while s and s.next and q and q.next and q.next.next:
                s = s.next
                q = q.next.next

                if s is q:
                    flag = True
                    break

        return flag