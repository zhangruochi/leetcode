from collections import deque


class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.elem)    

class Tree(object):
    def __init__(self,arr):
        self.arr = arr
        self.root = self.__generate_tree(arr,0)

    def __generate_tree(self, arr, cnt_index):
        """
        树的生成
        arr: 生成树的元素
        cnt_index: 当前根元素的索引
        """
        node = Node(arr[cnt_index])
        left_index, right_idnex = cnt_index * 2 + 1,cnt_index * 2 + 2
        if left_index < len(arr):
            node.left = self.__generate_tree(arr,left_index)
        else:
            node.left = None

        if right_idnex < len(arr):
            node.right = self.__generate_tree(arr,right_idnex)
        else:
            node.right = None
        return node

    # ------- 递归遍历 --------    

    def recursive_preorder(self,node):
        """
        递归先序遍历
        """
        if not node:
            return
        else:
            print(node,end = " ")  
            self.recursive_preorder(node.left)  
            self.recursive_preorder(node.right)

    
    def recursive_inorder(self,node):
        """
        中序遍历
        """        
        if not node:
            return 
        else:
            self.recursive_inorder(node.left)
            print(node,end = " ")
            self.recursive_inorder(node.right)

    def recursive_postorder(self,node):
        """
        后续遍历
        """
        if not node:
            return 
        else:
            self.recursive_postorder(node.left)
            self.recursive_postorder(node.right)
            print(node,end = " ")


        

    # ------- 迭代遍历 -------- 
    def non_recursive_preorder(self,node):
        """
        非递归前序遍历
        """
        if not node:
            return 

        stack = deque()
        stack.append(node)
        while stack:
            curr_node = stack.pop()
            if not curr_node:
                continue
            print(curr_node,end = " ")    
            stack.append(curr_node.right)
            stack.append(curr_node.left)

    def non_recursive_preorder2(self,node):
        """
        非递归前序遍历2
        """
        stack = deque()
        while stack or node:
            while node:
                print(node,end = " ")
                stack.append(node)
                node = node.left
            #当左子树为空，当前结点出栈，当前结点为出栈的元素    
            node = stack.pop()
            #当前结点改为当前结点的右子树
            node = node.right

    
    def non_recursive_inorder(self,node):
        """
        非递归中序遍历
        """
        stack = deque()
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            #当左子树为空，当前结点出栈，当前结点为出栈的元素    
            node = stack.pop()
            print(node,end = " ")
            #当前结点改为当前结点的右子树
            node = node.right
        

    def non_recursive_postorder(self,node):
        stack = deque()
        last_visit = None
        index = 0
        while len(stack) or node:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) != 0:
                node = stack[-1]
                if not node.right or node.right ==  last_visit:
                    last_visit = stack.pop()
                    print(last_visit, end = " ")
                    node = None
                else:
                    node = node.right

                    

    def recursive_level_traversal(self, node):
        """
        层次遍历
        """
        queue = deque()
        queue.append(node)
        while queue:
            curr_node = queue.popleft()
            print(curr_node,end = " ")
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)




if __name__ == '__main__':
    tree = Tree([0,1,2,3,4,5,6,7,8,9,10])
    print("递归前序遍历: ")   
    tree.recursive_preorder(tree.root)
    print("\n递归中序遍历: ")
    tree.recursive_inorder(tree.root)
    print("\n递归后序遍历: ")
    tree.recursive_postorder(tree.root)

    print("\n非递归前序遍历: ")
    tree.non_recursive_preorder(tree.root)

    print("\n非递归前序遍历2: ")
    tree.non_recursive_preorder2(tree.root)

    print("\n非递归中序遍历: ")
    tree.non_recursive_inorder(tree.root)

    print("\n非递归后序遍历: ")
    tree.non_recursive_postorder(tree.root)

    print("\n层次遍历: ")
    tree.recursive_level_traversal(tree.root)


                



