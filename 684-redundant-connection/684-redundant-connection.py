class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent= [i for i in range(n+1)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(p,q):
            rootP, rootQ = find(p), find(q)
            
            if rootP == rootQ:
                return False
            
            parent[rootP] = rootQ
            return True
            
        for edge in edges:
            if not union(edge[0],edge[1]):
                return edge
        
        return []
            