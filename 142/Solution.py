"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

class Solution(object):
    # space complexity O(n)
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = quick = head
        while slow and quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                start = head
                while start != quick:
                    start = start.next
                    quick = quick.next
                return start
            
        return None