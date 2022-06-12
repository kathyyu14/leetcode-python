class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        far = 0
        for i in range(n-1):
            far = max(far, i + nums[i])
            print(far)
            if far <= i:
                return False
            
        return far >= n - 1