class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [-1] * (n + 1)
        prefix[0] = 0
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        for i in range(1, n + 1):
            left = prefix[i-1] - prefix[0]
            right = prefix[n] - prefix[i]
            if left == right:
                return i - 1
        
        return -1