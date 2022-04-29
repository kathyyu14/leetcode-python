class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return res
        track = []
        
        def backtrack(left, right, track):
            if left > right:
                return 
            
            if left < 0 or right < 0:
                return
            
            
            if left == 0 and right == 0:
                res.append(''.join(track))
            
            
            # left
            track.append('(')
            backtrack(left-1, right, track)
            track.pop()
            
            #right
            track.append(')')
            backtrack(left, right-1, track)
            track.pop()
        
        backtrack(n, n, track)
        return res
            