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

        '''
        我们之前知道区间和的公式等于k = sum[j] - sum[i - 1], 我们通过简单的移项可以得出这个公式sum[i - 1] = sum[j] - k。
        
        我们在遍历nums时，可以获得当前的前缀和，当前的前缀和减去k，可以得到我们需要找的另一个前缀和的大小，如果hash之中有记录，我们只需要获取hash中的记录，就可以知道有多少区间和等于k了。
        '''
        
# @lc code=end

