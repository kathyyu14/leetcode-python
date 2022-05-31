class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        self.trackSum = 0
        
        if len(candidates) == 0:
            return res
        
        candidates.sort()
        
        def backtrack(nums, start, track):
            #base case
            if self.trackSum == target:
                    res.append(track.copy())
                    return
            if self.trackSum > target:
                    return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                track.append(nums[i])
                self.trackSum += nums[i]
                backtrack(nums, i+1, track)
                track.pop()
                self.trackSum -= nums[i]
        
        backtrack(candidates, 0, track)
        return res
    