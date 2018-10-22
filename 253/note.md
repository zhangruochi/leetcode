## 思路

- 扫描整个时间段，遇到起始时间 count + 1, 遇到结束时间 count - 1
- count 维护着每个时间所需要的 room 数量
- max(max_room,count) 即表示一共需要的 room 数量