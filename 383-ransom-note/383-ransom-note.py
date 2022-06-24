class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = collections.Counter(magazine)
        
        for n in ransomNote:
            if n in count:
                count[n] -= 1
                if count[n] == 0:
                    del count[n]
            else:
                return False
        
        return True