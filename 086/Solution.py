# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        pre = dummy = ListNode(0)
        dummy.next = head
        while pre.next and pre.next.val < x:
            pre = pre.next
    
        right = pre.next
        if not right:
            return head
        
        cur = right.next
        while cur:
            if cur.val >= x:
                right.next = cur
                right  = right.next
                cur = cur.next
            else:
                tmp = cur
                cur = cur.next
                tmp.next = pre.next
                pre.next = tmp
                pre = pre.next  
                
        right.next = None
        
        return dummy.next
                
    


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def partition(self, head: ListNode, x: int) -> ListNode:
        
#         pre = dummy = ListNode(0)
#         dummy.next = head
#         while pre.next and pre.next.val < x:
#             pre = pre.next
        
#         right = pre.next
#         if not right:
#             return head
        
#         cur = right.next
#         index = 0
#         while cur:
#             if cur.val >= x:
#                 right.next = cur
#                 right  = right.next
#                 cur = cur.next
#             else:
#                 tmp = cur
#                 cur = cur.next
#                 tmp.next = pre.next
#                 pre.next = tmp
#                 pre = pre.next    
#             index += 1
        
#         right.next = None

#         return head
# if __name__ == '__main__':
#     head = ListNode(1)
#     cur = head
#     cur.next = ListNode(4)
#     cur = cur.next
#     cur.next = ListNode(3)
#     cur = cur.next
#     cur.next = ListNode(2)
#     cur = cur.next
#     cur.next = ListNode(5)
#     cur = cur.next
#     cur.next = ListNode(2)

#     s = Solution()
#     head = s.partition(head,3)

#     while head:
#         print(head.val)
#         head = head.next