##  思路
- 首先用BFS遍历一遍图，把所有的结点保存在 set 里面
- 然后对set里每个node, 新建对应的 UndirectedGraphNode,  用 table 保存 node 和 UndirectedGraphNode 的对应关系
- 再遍历一遍 set, 对每个 node 以及其对应的 neighbors. 将该关系复制到 每个 node 对应的 UndirectedGraphNode