class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m:
                return 
            if grid[i][j] == 1:
                return
            
            grid[i][j] = 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # 把边缘的岛屿变成水
        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)
        
        # 计算岛屿数量
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i,j)
        
        return res