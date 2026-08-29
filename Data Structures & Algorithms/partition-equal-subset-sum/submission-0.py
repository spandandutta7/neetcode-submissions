class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summed = sum(nums)
        if summed % 2 != 0:
            return False
        target = summed/2


        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i >= len(nums):
                return False

            return dfs(i+1, target - nums[i]) or dfs(i+1, target)
        
        return dfs(0, target)
            
        