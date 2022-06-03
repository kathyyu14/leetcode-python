class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        self.count = n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(p,q):
            rootP = find(p)
            rootQ = find(q)
            
            if rootP == rootQ:
                return
            parent[rootQ] = rootP
            self.count -= 1
        
        def count():
            return self.count
        
        for e in edges:
            union(e[0],e[1])
        
        return count()
            
            