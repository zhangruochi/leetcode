"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{}".format(self.val)    

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur_a,cur_b,count_a,count_b,start = headA,headB,0,0,None

        if not (headA and headB):
            return None



        while cur_a.next:
            cur_a = cur_a.next
            count_a += 1

        while cur_b.next:
            cur_b = cur_b.next
            count_b += 1

        cur_a = headA
        cur_b = headB

        if count_a > count_b:
            diff = count_a - count_b
            while diff:
                cur_a = cur_a.next
                diff -= 1
        else:
            diff = count_b - count_a
            while diff:
                cur_b = cur_b.next
                diff -= 1


        while cur_a and cur_b:

            if cur_a is cur_b:
                if not start:
                    start = cur_a
            else:
                start = None
            
            cur_a = cur_a.next
            cur_b = cur_b.next    

        return start     

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        len_a, len_b = 0,0
        cur_a, cur_b = headA, headB
        
        while cur_a:
            len_a += 1
            cur_a = cur_a.next
        
        while cur_b:
            len_b += 1
            cur_b = cur_b.next
        
        dif = abs(len_a - len_b)
        if len_a > len_b:
            while dif:
                headA = headA.next
                dif -= 1
        else:
            while dif:
                headB = headB.next
                dif -= 1
        
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA if headA == headB else None

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next = d
    
    b.next = c
    c.next = d

    d.next = e


    print(Solution().getIntersectionNode(a,b))













