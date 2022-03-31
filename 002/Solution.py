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



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def add_carry(head,carry):
            dummy = cur = ListNode(0)
            dummy.next = head       
            while cur.next:
                carry,cur.next.val = divmod((cur.next.val + carry),10)
                cur = cur.next
                    
            if carry:
                cur.next = ListNode(carry)
            
            return dummy.next
        
        
        carry = 0
        head = l1
        
        dummy_l1 = cur_l1 =  ListNode(0)
        dummy_l1.next = l1
        dummy_l2 = cur_l2 = ListNode(0)
        dummy_l2.next = l2
        
        while cur_l1.next and cur_l2.next:
            carry,cur_l1.next.val = divmod((cur_l1.next.val + cur_l2.next.val + carry),10)
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
        

        
        if not carry:
            if not cur_l1.next:
                cur_l1.next = cur_l2.next                
        else:
            if not cur_l1.next and not cur_l2.next:
                cur_l1.next = ListNode(carry)
            elif not cur_l1.next:
                add_carry(cur_l2.next,carry)
                cur_l1.next = cur_l2.next
            else:
                add_carry(cur_l1.next,carry)
                
        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def list2num(head):
            num = 0
            mul = 1
            while head:
                num += head.val * mul
                mul *= 10
                head = head.next
            
            return num

        def str2list(num):
            dummy = tail = ListNode(0)
            if num == 0:
                return dummy
            while num:
                digit = num % 10
                num = num // 10
                tail.next = ListNode(digit)
                tail = tail.next
            return dummy.next

        num1 = list2num(l1)
        num2 = list2num(l2)

        return str2list(num1+num2)