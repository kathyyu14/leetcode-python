class Solution:
    def isHappy(self, n: int) -> bool:
        def getSqureSum(num):
          total = 0
          while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
          return total
        
        fast, slow = n, n
        while True:
          fast = getSqureSum(getSqureSum(fast))
          slow = getSqureSum(slow)
          if fast == slow:
            break
        
        return slow == 1