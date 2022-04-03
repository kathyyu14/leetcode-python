#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''#1
        return len(set(nums)) < len(nums)'''

        #2
        result = set()
        for i in range(len(nums)):
            if nums[i] in result:
                return True
            result.add(nums[i])
            
        return False

        '''
        Use the set to solve the problem
        hashTable contains each elements
        sorted list : num[I] == num[j]
        '''


# @lc code=end

