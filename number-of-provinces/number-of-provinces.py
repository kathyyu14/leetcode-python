class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        self.count = n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(p,q):
            rootp, rootq = find(p), find(q)
            
            if rootp == rootq:
                return
            
            parent[rootp] = rootq
            self.count -= 1
            
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    union(i,j)
        
        return self.count