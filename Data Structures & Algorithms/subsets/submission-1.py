class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        buildPath = []

        def backtrack(i):
            
            if i == len(nums):
                result.append(buildPath.copy())
                return
            
            backtrack(i + 1)

            buildPath.append(nums[i])
            backtrack(i + 1)
            buildPath.pop()

        backtrack(0)
        return result