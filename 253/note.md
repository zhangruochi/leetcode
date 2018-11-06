## 思路

- 扫描整个时间段，遇到起始时间 count + 1, 遇到结束时间 count - 1
- count 维护着每个时间所需要的 room 数量
- max(max_room,count) 即表示一共需要的 room 数量


**注意开始时间和结束时间相同的时候，不用算需要两个房间。所以用 points.sort() 而不用 points.sort(key = lambda x:x[0]), points.sort() 会先排第一个，再排第二个。**