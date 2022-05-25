class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        curr = self.root
        curr.score += delta
        for c in key:
            curr = curr.children.setdefault(c, TrieNode())
            curr.score += delta
        

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.score
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)