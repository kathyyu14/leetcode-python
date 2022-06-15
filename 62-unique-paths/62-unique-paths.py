class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]
        
        def dp(i, j):
            if i == 0 or j == 0:
                return 1
            
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            
            if memo[i][j] > 0:
                return memo[i][j]
            
            memo[i][j] = dp(i - 1, j) + dp(i, j - 1)
            
            return memo[i][j]
        
        return dp(m-1, n-1)
            