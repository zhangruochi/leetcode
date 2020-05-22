"""
编写一个函数，检查输入的链表是否是回文的。

 

示例 1：

输入： 1->2
输出： false 
示例 2：

输入： 1->2->2->1
输出： true 
 

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:


        def reverse(root):
            dummy = ListNode(0)
            dummy.next = cur = root

            while cur.next:
                tmp = cur.next.next
                cur.next.next = dummy.next
                dummy.next = cur.next
                cur.next = tmp
        
            return dummy.next



        slow = quick = left_root = head
 
        # length 0 or 1
        if not quick or not quick.next:
            return True

        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next

    
        right_root = reverse(slow)


        # while right_root:
        #     print(right_root.val)
        #     right_root = right_root.next


        while right_root and left_root:
            if right_root.val != left_root.val:
                return False
        
            right_root = right_root.next
            left_root = left_root.next
        
        return True

            