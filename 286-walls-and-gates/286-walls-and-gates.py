class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q = deque()
        ROWS = len(rooms)
        COLS = len(rooms[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    # row, col, distance
                    q.append((row, col, 0))
        
        # BFS
        visit = set()
        while q:
            row, col, distance = q.popleft()
            
            for r, c in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or (rooms[r][c] in [0,-1]) or (r, c) in visit:
                    continue
                rooms[r][c] = min(rooms[r][c], distance + 1)
                q.append((r, c, rooms[r][c]))
                visit.add((r,c))

# Time complexity - O(mn)