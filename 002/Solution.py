# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def add_carry(self,p,carry):
        while carry and p:
            carry,val = divmod(p.val+carry,10)
            p.val = val
            if not p.next:
                end = p
            p = p.next
        if carry:
            end.next = ListNode(carry)
        
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        
        p1,p2,carry = l1,l2,0
        while p1 and p2:
            carry,val = divmod(p1.val+p2.val+carry,10)
            p1.val = val
            if not p1.next:
                end = p1        
            p1 = p1.next
            p2 = p2.next
        
        if not carry:
            if not p1:
                end.next = p2
        else:
            if not p1 and not p2:
                end.next = ListNode(carry)
            elif not p1:
                self.add_carry(p2,carry)
                end.next = p2
            else:
                self.add_carry(p1,carry)
        return l1
