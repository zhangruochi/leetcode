"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。


示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

限制：

0 <= 节点个数 <= 5000


注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = cur = head

        while cur.next:
            tmp = cur.next.next
            cur.next.next = dummy.next
            dummy.next = cur.next
            cur.next = tmp
        
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return head

        dummy = ListNode()
        dummy.next  = tail = head

        while head.next:
            tmp = head.next.next

            head.next.next = dummy.next
            dummy.next = head.next

            head.next = tmp

        
        return dummy.next



        