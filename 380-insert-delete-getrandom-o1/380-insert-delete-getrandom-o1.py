class RandomizedSet:

    def __init__(self):
        self.randomMap = {}
        self.array = []
        

    def insert(self, val: int) -> bool:
        if val in self.randomMap:
            return False
        self.randomMap[val] = len(self.array)
        self.array.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.randomMap:
            return False
        lastElement, idx = self.array[-1], self.randomMap[val]
        self.array[idx], self.randomMap[lastElement] = lastElement, idx
        self.array.pop()
        del self.randomMap[val]
        
        return True
        

    def getRandom(self) -> int:
        ram = random.randint(0, len(self.array)-1)
        return self.array[ram]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

