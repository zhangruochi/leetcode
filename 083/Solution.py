"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)    

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
            
        cur = prev = head
        while cur.next:
            if cur.val == cur.next.val:
                if cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
            else:
                cur = cur.next
        return head                   

if __name__ == '__main__':
    one = ListNode(1)
    one2 = ListNode(1)
    two = ListNode(2)

    one.next = one2
    one2.next = two

    print(Solution().deleteDuplicates(one))


                