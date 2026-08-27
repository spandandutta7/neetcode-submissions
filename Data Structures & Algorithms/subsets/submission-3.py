class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, currentPath):
            if i == len(nums):
                result.append(currentPath.copy())
                return
            
            backtrack(i+1, currentPath)

            currentPath.append(nums[i])
            backtrack(i+1, currentPath)
            currentPath.pop()
        
        backtrack(0, [])
        return result
            

        