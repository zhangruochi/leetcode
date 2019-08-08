# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
            
        dummy = ListNode(0)
        dummy.next = head
        pre_m = cur_n = dummy
        
        for i in range(m-1):
            pre_m = pre_m.next
        
        for i in range(n+1):
            cur_n = cur_n.next
            

        tail = pre_m.next
        
        for i in range(n-m):
            tmp = tail.next
            tail.next = tmp.next
            tmp.next = pre_m.next
            pre_m.next = tmp
        
        tail.next = cur_n
        
        return dummy.next