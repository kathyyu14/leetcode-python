class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = collections.defaultdict(list)
        
        for s in strs: 
            hashMap[tuple(sorted(s))].append(s)
        
        return hashMap.values()

            