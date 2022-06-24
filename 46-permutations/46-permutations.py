class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def dfs(track):
            if len(track) == n:
                res.append(track.copy())
                return
            
            for i in range(n):
                if nums[i] in track:
                    continue
                    
                track.append(nums[i])
                dfs(track)
                track.pop()
            
        dfs([])
        return res