class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return (dfs(i+1, j) +
                    dfs(i-1, j) +
                    dfs(i, j+1) +
                    dfs(i, j-1) + 1
                   )
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
        
        return res