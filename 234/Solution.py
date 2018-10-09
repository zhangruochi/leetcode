"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)    

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        cur = head
        valus = []
        while cur:
            valus.append(cur.val)
            cur = cur.next

 
        tail = head 
        while head.next:
            tmp = head.next
            head.next = head.next.next
            tmp.next = tail
            tail = tmp

        index = 0    
        while tail:
            if tail.val != valus[index]:
                return False

            tail = tail.next
            index+= 1
        return True  

    def reverse(self,midpoint):
        tail = head = midpoint.next
        while head.next:
            tmp = head.next
            head.next = head.next.next
            tmp.next = tail
            tail = tmp

        midpoint.next = tail
        return midpoint        

    def isPalindrome2(self, head):

        if not head or not head.next:
            return True   

        slow = quick = head
        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next

        slow = self.reverse(slow)
        slow = slow.next

        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next    
        return True                 


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(1)

    a.next = b
    b.next = c
    c.next = d

    print(Solution().isPalindrome2(a))    

