#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def reverse(List):
            i = 0
            j = len(List) -1
            while i < j:
                temp = List[i]
                List[i] = List[j]
                List[j] = temp
                i += 1
                j -= 1
            
        
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        for row in matrix:
            reverse(row)
        
# @lc code=end

