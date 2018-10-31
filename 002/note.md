## 思路
- 两个链表相加部分
    - 当两个链表都存在才相加，为了降低空间复杂度，将结果保存在链表l1
    - 如果l1将要为None, 用 end 记录最后一个l1, 方便连接后序l2链表carry

```Python
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
```
- 剩余链表加 carry 部分
    - 分情况讨论
    - 没有 carry: 
        - 如果p1不存在，需要将p2连接end后面
        - 如果p2不存在或者p1,p2都不存在，不用管。
    - 有carry:
        - 如果p1,p2都不存在，添加一个新listnode(carry)
        - 如果只有p1不存在，用 carry 和 p2相加, 并把p2连接到 end 后面
        - 如果只有p2不存在，用 carry 和 p1相加
```Python
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
```


- list 和 carry 相加部分
    - list 和 carry 都存在, 一直相加
    - 加完后 carry 还存在，添加新listnode(carry)

```Python
def add_carry(self,p,carry):
    while carry and p:
        carry,val = divmod(p.val+carry,10)
        p.val = val
        if not p.next:
            end = p
        p = p.next
    if carry:
        end.next = ListNode(carry)
```