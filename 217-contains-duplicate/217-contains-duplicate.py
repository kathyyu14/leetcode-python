class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        
        return False

main = Solution().containsDuplicate([1,1,1,1,2])
print(main)