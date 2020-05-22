"""
给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

 

示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：假设这些数位是正向存放的，请再做一遍。

示例：

输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-lists-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:


        def helper(l1,l2,carry):

            if not l1 and not l2:
                if carry:
                    return ListNode(carry)
                else:
                    return None

            if not l1:
                return helper(l2, ListNode(carry), 0)
            
            if not l2 :
                return helper(l1, ListNode(carry), 0)

            carry, l1.val = divmod(l1.val + l2.val + carry, 10)
            l1.next = helper(l1.next, l2.next, carry)

            return l1

        return helper(l1,l2, 0)

