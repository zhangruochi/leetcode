# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def merge(self,list1,list2):
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return dummy.next
                    

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        middle = slow.next
        slow.next = None
        
        return self.merge(self.sortList(head),self.sortList(middle)) 


class Solution:

    def merge(self,list1,list2):
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        while tail.next : tail = tail.next

        return dummy.next,tail

    # split the list into two parts, first n elements and the rest
    def split(self,head,n):
        while n > 1 and head:
            head = head.next
            n -= 1
        rest = head.next if head else None
        if head:
            head.next = None
        return rest    
            
                    

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        length = 0
        cur = head
        while cur: 
            length += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head

        n = 1
        while n < length:        
            cur = dummy.next
            tail = dummy

            while cur:
                first = cur
                cur = self.split(first,n)
                second = cur
                cur = self.split(second,n)

                merged = self.merge(first,second)
                tail.next = merged[0]
                tail = merged[1]

            n = n << 1
        return dummy.next
        
