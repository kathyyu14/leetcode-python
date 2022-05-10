class Solution:
    def minSubArrayLen(self, s: int, arr: List[int]) -> int:
        left, right = 0,0
        target_sum = 0
        min_len = float('inf')
        while right < len(arr):
            target_sum += arr[right]
            right +=1
            while target_sum >= s:
                min_len = min(min_len, right-left)
                target_sum -= arr[left]
                left +=1
        return min_len if min_len != float('inf') else 0