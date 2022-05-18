class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m*n-1
        
        while left <= right:
            mid = left + (right-left) //2
            if matrix[mid//n][mid%n] > target:
                right = mid - 1
            elif matrix[mid//n][mid%n] < target:
                left = mid + 1
            else:
                return True
        
        return False