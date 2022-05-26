class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        track = set()
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if(min(r,c)< 0 or r >= rows or c >= cols or word[i]!= board[r][c] or (r,c) in track):
                return False
            
            track.add((r,c))
            res = (
                backtrack(r,c+1,i+1) or
                backtrack(r,c-1,i+1) or
                backtrack(r+1,c,i+1) or
                backtrack(r-1,c,i+1)
            )
            track.remove((r,c))
            
            return res
        
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False
    
    
    
    
        