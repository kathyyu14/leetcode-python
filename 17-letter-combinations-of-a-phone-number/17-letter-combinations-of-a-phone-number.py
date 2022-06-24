class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digitMap = {0:"", 1:"", 2:"abc", 3:"def", 4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        digitArr = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        track = []
        
        if len(digits) == 0:
            return res
        
        def dfs(i, track):
            if len(track) == len(digits):
                res.append("".join(track))
                return

            for c in digitArr[int(digits[i])]:
                track.append(c)
                dfs(i + 1, track)
                track.pop()
        
        dfs(0, track)
        return res
                    
                