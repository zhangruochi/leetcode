## 思路

- 自下而上的归并排序(因为使用递归，空间复杂度为log(n))
    ```Python
    ## 按照大小顺序合并两个排序好的链表，用双指针
    def merge(self,list1,list2):
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## 递归出口
        if not head or not head.next:
            return head

        ## 利用快慢指针知道链表的中点    
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        ## 断开链表    
        middle = slow.next
        slow.next = None
        
        ##  递归调用
        return self.merge(self.sortList(head),self.sortList(middle)) 
    ```

- 自上而下的递归排序 空间复杂度为O(1)
    ```Python
    # 合并两个排序好的链表，链表头和链表尾
    def merge(self,list1,list2):
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        while tail.next : tail = tail.next

        return dummy.next,tail

    # split the list into two parts, first n elements and the rest
    def split(self,head,n):
        while n > 1 and head:
            head = head.next
            n -= 1
        rest = head.next if head else None
        if head:
            head.next = None
        return rest    
            
                    

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # 求链表的长度    
        length = 0
        cur = head
        while cur: 
            length += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head

        n = 1 # (n=2^0,2^1,2^2,2^3......)
        while n < length:        
            cur = dummy.next
            tail = dummy

            while cur:
                # 连续断开长度为n的两部分
                first = cur
                cur = self.split(first,n)
                second = cur
                cur = self.split(second,n)
                # 合并链表
                merged = self.merge(first,second)
                tail.next = merged[0]
                tail = merged[1]

            n = n << 1
        return dummy.next
    ```










