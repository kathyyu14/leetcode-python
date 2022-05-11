class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right = 0,0
        hashMap = {}
        max_len = 0
        while right < len(s):
            char = s[right]
            hashMap[char] = hashMap.get(char, 0) + 1
            right += 1

            while len(hashMap) > k:
                left_char = s[left]
                print(hashMap)
                if left_char in hashMap:
                    hashMap[left_char] -= 1
                if hashMap[left_char] == 0:
                    del hashMap[left_char]
                left += 1
            max_len = max(max_len, right-left)
        
        return max_len