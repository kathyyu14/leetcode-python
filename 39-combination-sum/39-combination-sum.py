class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        
        def backtrack(start, track, remain):
            if remain == 0:
                res.append(list(track))
                return
            elif remain < 0:
                return
            
            
            for i in range(start, len(candidates)):
                track.append(candidates[i])
                backtrack(i, track, remain - candidates[i])
                track.pop()
        
        backtrack(0, track, target)
        return res
            