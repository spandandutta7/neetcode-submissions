class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        bottom, top = 0, m - 1
        selRowInd = None

        while bottom <= top:
            mid = bottom + ((top - bottom) // 2)

            if target >= matrix[mid][0] and target <= matrix[mid][n - 1]:
                selRowInd = mid
                break
            
            elif target < matrix[mid][0]:
                top = mid - 1
            else:
                bottom = mid + 1
        
        if selRowInd is None:
            return False
        
        left, right = 0, n - 1
        while left <= right:
            mid = left + ((right - left) // 2)

            if matrix[selRowInd][mid] == target:
                return True
            elif matrix[selRowInd][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False