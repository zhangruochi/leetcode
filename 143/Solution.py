# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return head
        
        all_nodes = []
        cur = head
        count = 0
        while cur:
            all_nodes.append(cur)
            cur = cur.next
            count += 1
        
        ordered_nodes = []
        for i in range(count//2):
            ordered_nodes.append(all_nodes[0+i])
            ordered_nodes.append(all_nodes[-1-i])
            
        if count % 2 != 0:
            ordered_nodes.append(all_nodes[count//2])
        
        for i in range(count-1):
            ordered_nodes[i].next = ordered_nodes[i+1]
        
        ordered_nodes[-1].next = None
        
        return ordered_nodes[0]
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return head
        
        
        def reverse(head):
            if not head:
                return head
            
            dummy = ListNode(0)
            dummy.next = head
            
            tail = dummy
            while head.next:
                tmp = head.next
                head.next = tmp.next
                tmp.next = tail.next
                tail.next = tmp
            return dummy.next
        
    
        dummy = ListNode(0)
        dummy.next = head
        slow = quick = dummy
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            
        reversed_list_head = reverse(slow.next)
        
#         while reversed_list_head:
#             print(reversed_list_head.val)
#             reversed_list_head = reversed_list_head.next
        
        
        slow.next = None
        
        cur_left = dummy.next
        while cur_left and reversed_list_head:
            tmp_cur = cur_left.next
            tmp_reversed_list_head = reversed_list_head.next
            
            cur_left.next = reversed_list_head
            reversed_list_head.next = tmp_cur
            
            cur_left = tmp_cur
            reversed_list_head = tmp_reversed_list_head
            
        
        return dummy.next

        
            
        
        
            
        
        
       
        
        
        