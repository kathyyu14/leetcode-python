class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        
        for i in range(n-1, -1, -1):
            
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            res[i] = 0 if len(stack) == 0 else stack[-1] - i
            stack.append(i)
        
        return res