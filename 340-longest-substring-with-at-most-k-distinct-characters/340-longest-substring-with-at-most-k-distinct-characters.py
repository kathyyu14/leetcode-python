class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        res = 0
        hashMap = {}
        
        for i in range(len(s)):
            char = s[i]
            hashMap[char] = hashMap.get(char,0)+1
            
            while len(hashMap) > k:
                hashMap[s[left]] -=1
                if hashMap[s[left]] == 0:
                    hashMap.pop(s[left])
                left +=1
            res = max(res, i - left+1)
        return res
    