"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        #return "{}-> {}".format(self.val,self.next)
        return "{}->{}".format(self.val,self.next)     


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 or l2

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def merge_sublist(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            
            if l1.val < l2.val:
                l1.next = merge_sublist(l1.next, l2)
                return l1
            else:
                l2.next = merge_sublist(l1, l2.next)
                return l2
            
        return merge_sublist(l1, l2)
                
            

if __name__ == '__main__':
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l2 = ListNode (2)
    l2.next = ListNode(3)
    print(Solution().mergeTwoLists(l1, l2))
    


                


                






