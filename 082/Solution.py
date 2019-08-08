# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        count_dict = defaultdict(int)
        cur = head
        while cur:
            count_dict[cur.val] += 1
            cur = cur.next
        
        dup_set = set()
        
        for k,v in count_dict.items():
            if v > 1:
                dup_set.add(k)
        
        dummy = dummy_cur = ListNode(0)
        cur = head
        while cur:
            if cur.val not in dup_set:
                dummy_cur.next = cur
                dummy_cur = dummy_cur.next
            cur = cur.next
        
        dummy_cur.next = None
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        pre,cur = dummy,head
        while cur:
            if cur.next and cur.next.val == cur.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
            else:
                pre.next = cur
                pre = pre.next
                cur = cur.next
        
        pre.next = None
        return dummy.next
        