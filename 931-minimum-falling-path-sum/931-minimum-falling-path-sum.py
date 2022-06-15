class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = float('inf')
        memo = [[float('inf')] * cols for _ in range(rows)]
        
        def dp(r, c):
            if r < 0 or c < 0 or r == rows or c == cols:
                return float('inf')
            
            if r == 0:
                return matrix[0][c]
            
            if memo[r][c] != float('inf'):
                return memo[r][c]
            
            memo[r][c] = matrix[r][c] + min(
                dp(r-1, c-1),
                dp(r-1, c),
                dp(r-1, c+1)
            )
            
            return memo[r][c]
            
        
        for col in range(cols):
            res = min(res, dp(rows-1, col))
        
        return res