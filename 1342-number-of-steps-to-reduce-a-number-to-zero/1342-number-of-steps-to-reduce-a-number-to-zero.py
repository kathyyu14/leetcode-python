class Solution:
    def numberOfSteps(self, num: int) -> int:
        self.count = 0
        
        while num != 0:
            if num % 2 == 0:
                num = num//2
            else:
                num -= 1
            self.count +=1
            
        return self.count