"""
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:

We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

 
Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
"""






"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


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

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root:
            return 
        

        head = None
        tail = None

        prev = None

        def inorder(root):
            nonlocal head, tail, prev

            if not root:
                return 

            inorder(root.left)
            if not prev:
                prev = root
            else:
                prev.right = root
                root.left = prev
                prev = root

            if not head:
                head = root
            tail = root

            inorder(root.right)
            return 
        
        inorder(root)

        tail.right = head
        head.left = tail

        return head  
            
        