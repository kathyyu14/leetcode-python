class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = {}, {}
        for char in s1:
            need[char] = need.get(char, 0) + 1
        
        left, right, valid = 0, 0, 0
        
        while right < len(s2):
            c = s2[right]
            right += 1
            if need.get(c):
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
        
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                if need.get(d):
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
                
            
        