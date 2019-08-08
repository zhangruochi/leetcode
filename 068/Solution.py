# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
        
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return head
        
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        
        _,k = divmod(k,count)
            
        if k == 0:
            return head
        
        cur = head
        for i in range(count-k-1):
            cur = cur.next
        
        new_head = cur.next
        cur.next = None
        
        cur = new_head
        while cur.next:
            cur = cur.next
        
        cur.next = head
        
        return new_head
            
        
        