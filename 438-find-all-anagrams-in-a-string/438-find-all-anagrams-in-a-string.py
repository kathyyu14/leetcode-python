class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = collections.Counter(p)
        window = {}
        l, r = 0, 0
        res = []
        valid = 0
        
        
        while r < len(s):
            c = s[r]
            r += 1
                    
            if count.get(c):
                window[c] = window.get(c, 0) + 1
                if window[c] == count[c]:
                    valid += 1

            
            while r - l >= len(p):
                if valid == len(count):
                    res.append(l)
                
                d = s[l]
                l += 1
                if window.get(d):
                    if window[d] == count[d]:
                        valid -= 1     
                    window[d] -= 1
            
        return res