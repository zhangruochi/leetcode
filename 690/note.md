## 思路

- 利用一个 table 保存员工信息，方便后序查询。key 为 employee.id, value 为 employee
- 利用DFS, 没出栈一个员工，total += employee.importance, 同时把他的 employee.subordinates 入栈