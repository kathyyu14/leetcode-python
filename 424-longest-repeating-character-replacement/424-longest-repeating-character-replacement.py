class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, res = 0, 0
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if count[s[r]] > max_freq:
                max_freq = count[s[r]]
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res