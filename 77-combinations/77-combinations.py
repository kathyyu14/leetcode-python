class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(start, track):
            if len(track) == k:
                res.append(track.copy())
            
            for i in range(start, n):
                track.append(i+1)
                dfs(i+1, track)
                track.pop()
            
        dfs(0, [])
        return res
                
        