#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum and hash map
        
        count = 0
        sum0_i = 0
        hashMap = {0:1}
        
        for i in range(len(nums)):
            sum0_i += nums[i]
            sum0_j = sum0_i - k
            if sum0_j in hashMap.keys():
                count += hashMap[sum0_j]
            hashMap[sum0_i] = hashMap.get(sum0_i, 0) + 1
            
        return count
        
# @lc code=end

