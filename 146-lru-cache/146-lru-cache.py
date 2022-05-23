class LRUCache:

    def __init__(self, capacity: int):
        self.orderedDict = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.orderedDict:
            return -1
        self.orderedDict.move_to_end(key)
        return self.orderedDict[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.orderedDict:
            self.orderedDict.move_to_end(key)
        self.orderedDict[key]= value
        if len(self.orderedDict) > self.capacity:
            self.orderedDict.popitem(0)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)