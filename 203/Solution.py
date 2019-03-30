"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)    


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = cur = ListNode(0)
        while head:
            if head.val != val:
                cur.next = head
                cur = cur.next
                
            head = head.next
        
        cur.next = None
        return dummy.next
        

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None

        dummy = cur = ListNode(0)
        cur.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(1)


    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print(Solution().removeElements(None,1))





