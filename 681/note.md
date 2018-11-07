##  思路

1. 暴力枚举
    - 保存时间的元素为一个set, nums
    - 对当前时间每次加1，得到新时间，测试新时间的元素是否为nums的子集
    - 找到第一个满足条件的时间

2. DFS
    - time_diff 把时间化为分钟，然后比较两个时间的差，超过二十四小时要加上24小时
    - check 比较时间是否是正确的表达
    - 搜索所有可能的时间组合4^4 个
    - 找出时间差最小的

```Python
class Solution:
    
    def time_diff(self,time1,time2):
        diff = int(time1[:2]) * 60 + int(time1[-2:]) - (int(time2[:2]) * 60 + int(time2[-2:]))
        if diff <= 0:
            diff = 24 * 60 + diff
        return diff
    
    def check(self,time):
        if int(time[:2]) < 24 and int(time[:2]) >= 0  and time[-2:] <= "59":
            return True
        return False
                
    
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = time[:2] + time[-2:]
        best = time
        cur_min = 24*60
        
        def dfs(time,cur):
            nonlocal best,cur_min

            if len(cur) == 4:
                if self.check(cur):
                    diff = self.time_diff(cur,time)
                    if diff < cur_min:
                        cur_min = diff
                        best = cur
                return 

            for i in time:
                dfs(time,cur+i)
                
        dfs(time,"")
        return "{:02d}:{:02d}".format(int(best[0:2]),int(best[-2:]))
```