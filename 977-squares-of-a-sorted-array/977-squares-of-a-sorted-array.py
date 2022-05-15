class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        res = [0 for _ in range(n)]
        index = n-1
        
        while left <= right:
            squareL = nums[left] * nums[left]
            squareR = nums[right] * nums[right]
            
            if squareL < squareR:
                res[index] = squareR
                right -= 1
            else:
                res[index] = squareL
                left += 1
            index -= 1
        return res