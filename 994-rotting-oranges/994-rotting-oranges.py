class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs : queue
        n = len(grid)
        m = len(grid[0])
        q = collections.deque()
        time, fresh = 0, 0
        
        # count the fresh and get the rotten
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i,j])
                    
        #direction
        directions = [[0,1],[0,-1], [1,0], [-1,0]]
        
        # bfs
        while q and fresh > 0:
            for k in range(len(q)):
                i, j = q.popleft()
                for dr, dc in directions:
                    row, col = i+dr, j+dc
                    # make rotten
                    if (row in range(n) and
                        col in range(m) and
                        grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append([row,col])
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1