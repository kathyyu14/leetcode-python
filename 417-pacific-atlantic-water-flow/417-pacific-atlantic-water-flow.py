class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        res = []
        pac, atl = set(), set()
        
        def dfs(i,j,visit,prevHeight):
            if (i<0 or j<0 or i>=n or j>=m or
                (i,j) in visit or
                heights[i][j] < prevHeight
            ):
                return
            visit.add((i,j))
            dfs(i+1, j, visit, heights[i][j])
            dfs(i-1, j, visit, heights[i][j])
            dfs(i, j+1, visit, heights[i][j])
            dfs(i, j-1, visit, heights[i][j])
        
        # 第一列和最后一列
        for i in range(n):
            dfs(i,0,pac,heights[i][0])
            dfs(i,m-1,atl,heights[i][m-1])
        # 第一行和最后一行
        for j in range(m):
            dfs(0, j, pac, heights[0][j])
            dfs(n-1, j, atl, heights[n-1][j])
        
        for i in range(n):
            for j in range(m):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        
        return res
        