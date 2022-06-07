class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        # base case
        dp[0] = 0
        res = 0
        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1