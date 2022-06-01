class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        track = []
        
        def backtrack(start, track):
            if start >= len(s):
                res.append(track.copy())
                return 
            
            for i in range(start, len(s)):
                if isPali(s, start, i):
                    track.append(s[start:i+1])
                    backtrack(i+1, track)
                    track.pop()
        
        
        def isPali(s, l, r):
            while l<=r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        backtrack(0, track)
        return res