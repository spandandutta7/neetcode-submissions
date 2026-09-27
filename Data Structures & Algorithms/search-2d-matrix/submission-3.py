class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        topRow, bottomRow = 0, len(matrix) - 1

        while topRow <= bottomRow:
            mid = (topRow+bottomRow)//2

            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid])-1]:
                return self.searchRow(matrix[mid], target)
            elif target < matrix[mid][0]:
                bottomRow = mid - 1
            else:
                topRow = mid + 1
        
        return False
    
    def searchRow(self, arr, target):
            left, right = 0, len(arr)-1

            while left <= right:
                mid = (left+right)//2

                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid-1
            
            return False





        
        