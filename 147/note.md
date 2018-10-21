## 思路
- 用一个 cur.next 指针遍历当前链表，用cur.next 的原因是为了往前插入cur后，cur能记录cur.next.next
- 用一个 cur_max 记录链表所到位置的最大值，如果当前的值大于该值，不用从头搜索位置，如果小于改值，需要从头搜索位置。
- 创建一个新指针 find 搜索位置，同样用 find.next 搜索，方便 cur 插入到 find.next位置
- 因为要从第一个元素开始比较或者插入，为了插入逻辑一直，创建哨兵结点。

```Python

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        
        dummy = ListNode(0)
        dummy.next,cur,cur_max = head,head,head.val
        
        
        while cur.next:
            if cur.next.val >= cur_max:
                cur_max = cur.next.val
                cur = cur.next
                continue
                
            find = dummy
            while find.next.val < cur.next.val:
                find = find.next
            else:     
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = find.next
                find.next = tmp
                
        return dummy.next
```