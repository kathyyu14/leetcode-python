class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        res = 0
        hashMap = {}
        while right < len(s):
            char = s[right]
            right += 1
            hashMap[char] = hashMap.get(char, 0) + 1
            
            while hashMap[char] > 1:
                hashMap[s[left]] -= 1
                left += 1
            
            res = max(res, right-left)

        return res
        