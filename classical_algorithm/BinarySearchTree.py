class Node:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.key)    


class Tree:
    
    def __init__(self,root):
        self.root = root

    def print_all(self,node):
        if not node:
            return 
        print(node.key,end=" ")
        self.print_all(node.left)
        self.print_all(node.right)    


    def find(self,x,node):

        if not node:
            return None
        elif x == node.key:
            return node
        elif x < node.key:
            return self.find(x,node.left)
        else:
            return self.find(x,node.right)

    
    def find_parent(self,node,parent,x):
        if node is None:
            return False,node,parent
        if node.key == x:
            return True,node,parent
        if node.key > x:
            return self.find_parent(node.left, node, x)
        else:
            return self.find_parent(node.right, node, x)

    

     
    def find_max(self,node):
        if not node.right:
            return node
        else:
            return self.find_max(node.right)

    def find_min(self,node):
        if not node.left:
            return node
        else:
            return self.find_min(node.left)

    def insert(self,x):

        flag,node,parent = self.find_parent(self.root,self.root,x)
        if not flag:
            if x < parent.key:
                parent.left = Node(x)
            elif x > parent.key:
                parent.right = Node(x)    


        """
        if x < root.key:
            if root.left:
                self.insert(x,root.left)
            else:
                root.left = Node(x)    
        
        elif x > root.key:
            if root.right:
                self.insert(x,root.right)
            else:
                root.right = Node(x) 
        """          

    
    def delete(self,x):
        flag,node,parent = self.find_parent(self.root,self.root,x)
        if not flag:
            return 
        else:
            if not node.left and not node.right:
                if node == parent.left:
                    parent.left = None
                else:
                    parent.right = None    
                del node
            elif not node.left and node.right:
                if node == parent.left:
                    parent.left = node.right
                else:
                    parent.right = node.right  
                del node     
            elif not node.right and node.left:
                if node == parent.left:
                    parent.left = node.left
                else:
                    parent.right = node.left
                del node
            else:
                right_min = self.find_min(node.right)    
                tmp = right_min.key
                self.delete(tmp)
                node.key = tmp


                    
                    





if __name__ == '__main__':
    a = Node(17)  
    b = Node(5)
    c = Node(35)
    e = Node(2)
    f = Node(16)

    a.left = b
    a.right = c
    b.left = e
    b.right = f

    tree = Tree(a)
    tree.print_all(tree.root)
    print("")

    print("find: {}".format(tree.find(2,tree.root)))
    print("find max: {}".format(tree.find_max(tree.root)))
    print("find min: {}".format(tree.find_min(tree.root)))

    print("insert 3: ")
    tree.insert(3)
    tree.print_all(tree.root)
    print("")

    print("delete 5: ")
    tree.delete(5)
    tree.print_all(tree.root)

    








