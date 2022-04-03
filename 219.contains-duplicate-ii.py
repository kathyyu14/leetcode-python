#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
                
        #         for i in range(0, len(nums)):
        #             for j in range(max(i - k, 0), i):
        #                 if nums[i] == nums[j]: return True
                            
                            
        #         return False

        hashSet = set()
        for i in range(len(nums)):
            if nums[i] in hashSet: return True
            hashSet.add(nums[i])
            if len(hashSet) > k:
                hashSet.remove(nums[i - k])
                
        return False

        # hasp map to save the index
        '''
        
        dic = {}
            for i, v in enumerate(nums):
                if v in dic and i - dic[v] <= k:
                    return True
                dic[v] = i  
            return False
        '''
# @lc code=end

