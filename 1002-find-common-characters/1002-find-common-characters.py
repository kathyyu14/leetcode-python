class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = list(words[0])
        
        for i in range(1, len(words)):
            newCheck = []
            for w in words[i]:
                if w in check:
                    newCheck.append(w)
                    check.remove(w)
            check = newCheck
        
        return check