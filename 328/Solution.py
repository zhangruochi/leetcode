"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)
        



class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        odd = cur_odd = ListNode(-1)
        even = cur_even = ListNode(-2)

        flag = True
        while head:
            if flag:
                cur_odd.next = head
                cur_odd = cur_odd.next
            else:
                cur_even.next = head  
                cur_even = cur_even.next  
            head = head.next
            flag = not flag

        cur_odd.next = even.next    
        return odd.next


    def oddEvenList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        odd_tail,cur,even = head,head.next,head.next
        while cur and cur.next:
            
            odd_tail.next = cur.next
            cur.next = cur.next.next
            odd_tail = odd_tail.next
            odd_tail.next = even
            cur = cur.next


        return head

    

            

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print(Solution().oddEvenList2(a))














