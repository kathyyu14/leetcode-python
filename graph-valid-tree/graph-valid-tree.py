class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [1] * n
        self.count = n
        
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2: return
            
            if rank[p1] >rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            self.count -= 1
        
        def connect(n1, n2):
            return find(n1) == find(n2)
        
        def count():
            return self.count
                
        for e in edges:
            u = e[0]
            v = e[1]
            if connect(u,v):
                return False
            
            union(u,v)
            
        return self.count == 1
            
            