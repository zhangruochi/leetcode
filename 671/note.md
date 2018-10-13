## 思路

- 思路一:
    - 遍历整个二叉树，保存所有的结点
    ```Python
    def get_all_value(root,result):
            if root == None:
                return 
            else:
                result.append(root.val)
                get_all_value(root.left,result)    
                get_all_value(root.right,result)
    ```
    - 找到所有结点里第二大的数，没有则返回1
    ```Python
    def find_second(nodes):
            diff_nodes = set(nodes)
            if len(diff_nodes) <=1:
                return -1
            else:
                return sorted(list(diff_nodes))[1]
    ```
- 思路二:
    - 广度优先搜索
    - 整棵树的最小值为根节点的值
    - 广度优先搜索遍历整颗树，当前结点的值大于最小值小于第二小值时更新第二小值，其孩子结点不用再入栈
    - 当前结点不存在左右子树时，其孩子结点也不用再入栈
    - 入栈左右孩子结点
    ```Python
    def findSecondMinimumValue2(self,root):
        """广度优先搜索
        """

        if not root:
            return -1

        queue = deque()
        queue.append(root)
        
        min_node, second_min, found = root.val, float('inf'), False

        while queue:
            cur_node = queue.popleft()
            if cur_node.val > min_node and cur_node.val < second_min:
                second_min = cur_node.val
                found = True
                continue

            if not cur_node.left:
                continue

            queue.append(cur_node.left)
            queue.append(cur_node.right)

        return  second_min if found else -1
    ```

- 思路三
    - 深度优先搜索
    - 根节点的值为左右子树最小值
    - 对当前跟结点而言，如果左孩子结点的值大于最小值，返回当前值。如果左孩子结点的值不存在，返回 -1，如果左孩子结点的值等于根节点的值，递归调用左子树。
    - 右孩子结点的值同理
    ```Python
    def findSecondMinimumValue3(self,root):

        if not root:
            return -1

        min_num = root.val    

        def DFS(root,min_num):
            if not root:
                return -1
        
            if root.val > min_num:
                return root.val

            min_l = DFS(root.left,min_num)
            min_r = DFS(root.right,min_num)

            if min_l == -1:
                return min_r

            if min_r == -1:
                return  min_l    

            return min(min_l,min_r)
        
        return DFS(root,min_num)  
    ```