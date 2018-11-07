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
        