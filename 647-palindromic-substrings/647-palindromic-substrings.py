class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0
        n = len(s)
        
        def isPali(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                self.res += 1
                l -= 1
                r += 1
        
        for i in range(n):
            isPali(i, i)
            isPali(i, i+1)
        
        return self.res