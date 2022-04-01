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


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        dummy.next = head
        
        while cur.next and cur.next.next:
            f = cur.next
            s = f.next
            tmp = s.next
            
            cur.next = s
            f.next = tmp
            s.next = f
            
            cur = f
            
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = cur = ListNode()
        dummy.next = head

        while cur.next and cur.next.next:
            print(cur.val)

            nn = cur.next.next.next

            # 取
            f = cur.next
            s = cur.next.next

            # 断、连
            cur.next = s
            s.next = f
            f.next = nn

            cur = f
        
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

            


