## 思路

- 建立原结点和新结点的一一映射关系
- 则 table[cur].next = table.get(cur.next,None)