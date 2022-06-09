class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(numbers)):
            key = target - numbers[i]
            if numbers[i] in hashMap.keys():
                return [hashMap[numbers[i]]+1, i+1]
            hashMap[key] = i
        