"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)
            

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(0)
        dummy.next = head

        while cur.next:
            tmp = cur.next
            if not tmp.next:
                break
            cur.next = cur.next.next
            tmp.next = cur.next.next
            cur.next.next = tmp

            cur = cur.next.next

        return dummy.next 


if __name__ == '__main__':
    one = ListNode(1) 
    two = ListNode(2)     
    three = ListNode(3)
    four = ListNode(4)

    one.next = two
    two.next = three
    three.next = four

    print(Solution().swapPairs(one))

            


