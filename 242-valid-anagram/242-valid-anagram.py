class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i], 0) + 1
            mapT[t[i]] = mapT.get(t[i], 0) + 1
        
        for c in s:
            if mapS.get(c) != mapT.get(c):
                return False
        
        return True