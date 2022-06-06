class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        dp = 0
        dp1 = 0
        dp2 = 1
        
        for i in range(2, n+1):
            dp = dp1 + dp2
            dp1 = dp2
            dp2 = dp
        
        return dp