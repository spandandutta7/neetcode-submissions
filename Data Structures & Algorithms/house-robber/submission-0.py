class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(n):
            #Base CAse
            if n >= len(nums):
                return 0
            if cache[n] != -1:
                return cache[n]
            #Skip the current and go next
            case1 = dfs(n+1)

            #Rob the current and go n + 2
            case2 = nums[n] + dfs(n+2)
            
            cache[n] = max(case1, case2)
            return cache[n]
        
        return dfs(0)