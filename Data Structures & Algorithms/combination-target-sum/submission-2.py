class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        buildPath = []

        def dfs(total, i):
            if total > target or i == len(nums):
                return
            if total == target:
                result.append(buildPath.copy())
                return

            #Skip the number and move to the next
            dfs(total, i + 1)

            #Use the number and use it again
            buildPath.append(nums[i])
            dfs(total + nums[i], i)
            buildPath.pop()
        
        dfs(0, 0)
        return result
        