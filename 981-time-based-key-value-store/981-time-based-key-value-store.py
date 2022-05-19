class TimeMap:

    def __init__(self):
        self.timeMap = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        time = self.timeMap[key]
        if not time:
            return ""
        
        
        l, r = 0, len(time) -1
    
        while l <= r:
            m = l + (r-l)//2
            if time[m][1] == timestamp:
                return time[m][0]
            elif time[m][1] > timestamp:
                r = m-1
            else:
                l = m+1
        
        return "" if r < 0 else time[r][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)