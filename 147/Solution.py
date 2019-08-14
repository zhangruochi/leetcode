"""
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        
        dummy = ListNode(0)
        dummy.next,cur,cur_max = head,head,head.val
        
        
        while cur.next:
            if cur.next.val >= cur_max:
                cur_max = cur.next.val
                cur = cur.next
                continue
                
            find = dummy
            while find.next.val < cur.next.val:
                find = find.next
            else:     
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = find.next
                find.next = tmp
                
        return dummy.next



class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        cur = head
        while cur.next:
            pos = dummy
            while (pos.next is not cur.next) and (cur.next.val >= pos.next.val):
                pos = pos.next
            
            if pos is cur:
                cur = cur.next
                continue
            
            else:
                tmp = cur.next
                cur.next = tmp.next
                
                tmp.next = pos.next
                pos.next = tmp
            
        return dummy.next

        