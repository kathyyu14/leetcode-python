class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def longestCommon(w1, w2):
            m, n = len(w1), len(w2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if w1[i - 1] == w2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            
            return dp[m][n]
        
        
        lcs = longestCommon(word1, word2)
        return len(word1) - lcs + len(word2) - lcs