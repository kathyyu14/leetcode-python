class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                res = s[l:r+1] if len(res) < (r - l + 1) else res
                l -= 1
                r += 1
        
            
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res = s[l:r+1] if len(res) < (r - l + 1) else res
                l -= 1
                r += 1
        
        return res
            
            