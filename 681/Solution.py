class Solution:
    def nextClosestTime(self, time: str) -> str:
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ":"}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed for block in divmod(cur,60) for digit in divmod(block,10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))



from functools import cmp_to_key
class Solution:
    def is_valid(self,time):
        hour, minute = time.split(":")
        return int(hour) < 24 and int(minute) < 60
    
    def compare(self,t1,t2):
        h1, m1 = t1.split(":")
        h2, m2 = t2.split(":")
        if int(h1) > int(h2):
            return 1
        elif int(h1) < int(h2):
            return -1
        else:
            if int(m1) > int(m2):
                return 1
            elif int(m1) < int(m2):
                return -1
            else:
                return 0
    
    def nextClosestTime(self, time: str) -> str:
        chars = set([time[0],time[1],time[3],time[4]])
        all_times = []
        for h1 in chars: 
            for h2 in chars:
                for m1 in chars:
                    for m2 in chars:
                        t = "{}{}:{}{}".format(h1,h2,m1,m2)
                        if self.is_valid(t):
                            all_times.append(t)
        
        all_times.sort(key = cmp_to_key(lambda x,y:self.compare(x,y)))
        
        print(all_times)
        for index, t in enumerate(all_times):
            if t == time:
                break
        
        return all_times[(index+1)%len(all_times)]
        
        
                            
       
        
        


class Solution:
    
    def next_time(self,time):
        hour = int(time[:2])
        mini = int(time[-2:])
        carry = 0
        
        if mini + 1 == 60:
            mini = 0
            carry = 1
        else:
            mini = mini+1
        
        if hour + carry == 24:
            hour = 0
        else:
            hour = hour + carry
        
        return "{:02d}:{:02d}".format(hour,mini)
        
    
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = set(list(time))
        while True:
            time = self.next_time(time)
            if set(time) <= nums:
                break

        return time
        