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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head:
            return head

        cur = head
        visited = set()
        dups = set()

        while cur:
            if cur.val in visited:
                dups.add(cur.val)
            visited.add(cur.val)
            cur = cur.next

        cur = head

        dummy = ListNode(val = 0, next = None)
        tail = dummy
        while cur:
            if cur.val not in dups:
                tail.next = cur
                tail = tail.next
            cur = cur.next

        tail.next = None

        return dummy.next
        