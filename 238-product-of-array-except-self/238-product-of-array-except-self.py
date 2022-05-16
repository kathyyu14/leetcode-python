class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
            
        res = [0 for _ in range(n)]
        res[0] =suffix[1]
        res[n-1] = prefix[n-2]
        
        # 除了 nums[i] 自己的元素积就是 nums[i] 左侧和右侧所有元素之积
        for i in range (1,n-1):
            res[i] = prefix[i-1] * suffix[i+1]
        
        return res
            