class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        ballon = Counter("balloon")
        res = len(text)
        
        
        for c in ballon:
            print(countText[c], ballon[c])
            res = min(res, countText[c] // ballon[c])
        
        return res