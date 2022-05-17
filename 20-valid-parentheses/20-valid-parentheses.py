class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ")}]" and len(stack) != 0:
                d = stack.pop()
                if bracket == ")" and d != "(":
                    return False
                elif bracket == "}" and d != "{":
                    return False
                elif bracket == "]" and d != "[":
                    return False
                else:
                    continue
            stack.append(bracket)
        
        return len(stack) == 0
            
                