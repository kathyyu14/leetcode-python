# @before-stub-for-debug-begin
from python3problem242 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(nlogn) sort
        # return sorted(s) == sorted(t)
    
        # hashmap solution
        if len(s) != len(t):
            return False
            
        hashS, hashT = {},{}
        
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        
        for c in hashS:
            if hashS[c] != hashT.get(c, 0):
                return False
            
        return True
# @lc code=end

