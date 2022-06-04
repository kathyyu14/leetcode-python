class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for i in range(n)] for i in range(n)]
        
        def isValid(board, row, col):
            n = len(board)
            # 检查列冲突
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            
            # 检查右上方是否有皇后相互冲突
            for i,j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False
            
            # 检查左下方是否有皇后相互冲突
            for i,j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def backtrack(board, row):
            if row == len(board):
                # res.append(board.copy())
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            n = len(board[row])
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(board, row+1)
                board[row][col] = '.'
        
        backtrack(board, 0)
        return res
                    
            
        