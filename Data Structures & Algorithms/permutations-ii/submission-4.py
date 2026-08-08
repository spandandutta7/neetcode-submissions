class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        buildPath = []

        def backtrack(n):
            if len(buildPath) == len(nums):
                res.add(tuple(buildPath.copy()))
                return
            
            for i in range(len(nums)):
                if nums[i] != -100:
                    buildPath.append(nums[i])
                    nums[i] = -100
                    backtrack(n+1)
                    nums[i] = buildPath[-1]
                    buildPath.pop()
        
        backtrack(0)
        return list(res)
