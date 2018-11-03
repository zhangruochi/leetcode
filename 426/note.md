## 思路

- 采用中序遍历，在遍历过程中保存上一次访问的结点prev
- 每次遇到新结点，使得prev.right = root, root.left = prev, 这样就得到了每个节点的前后指针
- 还需要把头尾指针相连


```Python

class Solution:
    

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return 
        
        def inorder(root):
            nonlocal prev
            if not root:
                return 
            inorder(root.left)
            root.left = prev
            if prev != None:
                prev.right = root
            prev = root
            inorder(root.right)
            
            
        prev = None
        inorder(root)

        
        tail = root
        while tail.right:
            tail = tail.right
        
        head = root
        while head.left:
            head = head.left
        
        head.left = tail
        tail.right = head
        
        return head
        
```