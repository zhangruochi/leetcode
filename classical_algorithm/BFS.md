## 基本概念
1. 源点,从源点开始寻找可达的定点
2. 搜索时，划分三种状态，白灰黑（未发现，已找到，处理完）。
3. 初始为白色，每次找到白色，变为灰色并放入队列，出队列将灰色变为黑色。
4. BFS 可以形成以源点为根的树结构 => 广度优先树

## 时间分析
每个节点入队和出队一次, 循环总次数为0(V), 检查邻接表所有的次数为O(E), 总时间为 O(V+E)


## 最短路径(无权最短路径)
- 距离定义：从 s 到 v 经过的最少的边, 记为 d(s,v), 不可达 d(s,v) -> +inf
- 引理:
$$ \forall(u,v) \in E, \ d(s,v) \leq d(s,u) + 1$$



```Python
## 无向图
Graph = {0:[1,2],1:[0,2],2:[0,1,4],3:[2,4],4:[2,3]}

from collections import deque
def BFS_ON_DIRCT(Graph,src):
    if src not in Graph:
        return

    queue = deque([src])
    visited = set([src])

    while queue:
        cur = queue.pop()
        for node in Graph[cur]:
            ## 已经访问过则不入队
            if node not in visited:
                queue.append(node)
                ## 核心思想，入队的时候做标记
                visited.add(node)

    return visited

print(BFS_ON_DIRCT(Graph,0))





## 有向图

class Node:
    def __init__(self,name,parent = None, level = float("inf"), visited = False):
        self.name = name
        self.parent = parent
        self.level = level
        self.visited = visited  

    def __repr__(self):
        return "({},{},{})".format(self.name,self.level,self.visited)      


Graph2 = {0:[],1:[0,2],2:[0,4],3:[2],4:[2,3]}

node_0 = Node(0)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)

nodes = [node_0,node_1,node_2,node_3,node_4]


from collections import deque

def BFS_short_path(Graph,src):
    if not src in Graph:
        return 

    queue = deque([src])    
    nodes[src].parent,nodes[src].level, nodes[src].visited = nodes[src],0,True

    stack = []

    while queue:
        cur_node = queue.pop()
        stack.append(cur_node)

        for node in Graph[cur_node]:
            if not nodes[node].visited:
                queue.append(node)
                nodes[node].parent,nodes[node].level,nodes[node].visited = nodes[cur_node],nodes[cur_node].level+1, True

    all_path = []            
    for node in nodes:
        node.visited = False
    

    while stack:
        
        node = nodes[stack.pop()]
        if not node.visited:
            path = []
            while node.parent !=  node:
                path.append(node.name)
                node.visited = True
                node = node.parent
            path.append(node.name) 
            node.visited = True

            all_path.append(path)

    print(all_path)
                


BFS_short_path(Graph2,1)
```



```python
from collections import deque

def BFS(graph, s, t):
    visited = [None] * len(graph)
    prev = [-1] * len(graph)
    queue = deque()

    queue.append(s)
    visited[s] = True

    while queue:
        s = queue.popleft()
        for node in graph[s]:
            if not visited[node]:
                prev[node] = s
                if node == t:
                    return prev
                visited[node] = True
                queue.append(node)

    return None


def print_path(prev,s,t):
    if prev[t] != -1 and s != t:
        print_path(prev,s, prev[t])
    print(str(t), end = " ")




if __name__ == '__main__':
    g = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5,6],5:[2,4,7],6:[4,7],7:[5,6]}
    prev = BFS(g,0,7)
    print_path(prev,0,7)
```
1. visited是用来记录已经被访问的顶点，用来避免顶点被重复访问。如果顶点 q 被访问，那相应的 visited[q] 会被设置为 true。
2. queue是一个队列，用来存储已经被访问、但相连的顶点还没有被访问的顶点。因为广度优先搜索是逐层访问的，也就是说，我们只有把第 k 层的顶点都访问完成之后，才能访问第 k+1 层的顶点。当我们访问到第 k 层的顶点的时候，我们需要把第 k 层的顶点记录下来，稍后才能通过第 k 层的顶点来找第 k+1 层的顶点。所以，我们用这个队列来实现记录的功能。
3. prev用来记录搜索路径。当我们从顶点 s 开始，广度优先搜索到顶点 t 后，prev 数组中存储的就是搜索的路径。不过，这个路径是反向存储的。prev[w] 存储的是，顶点 w 是从哪个前驱顶点遍历过来的。比如，我们通过顶点 2 的邻接表访问到顶点 3，那 prev[3] 就等于 2。为了正向打印出路径，我们需要递归地来打印，你可以看下 print() 函数的实现方式。
