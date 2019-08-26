from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_table = defaultdict(list)

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_table[key].append((timestamp,value))
    

    def get(self, key: str, timestamp: int) -> str:
                
        values = self.hash_table[key]
        
        low,high,n = 0,len(values)-1,len(values)-1
        
        while low <= high:
            mid = low + (high - low) // 2
            if values[mid][0] > timestamp:
                high = mid - 1
            else:
                if mid ==n  or values[mid+1][0] > timestamp:
                    return values[mid][1]
                else:
                    low = mid + 1
        
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)