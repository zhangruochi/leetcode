#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next

        return head
