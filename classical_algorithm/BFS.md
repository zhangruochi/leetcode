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