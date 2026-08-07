class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        buildPath = []

        def backtrack(n, hashSet):
            if len(buildPath) == len(nums):
                result.append(buildPath.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in hashSet:
                    hashSet.add(nums[i])
                    buildPath.append(nums[i])
                    backtrack(i+1, hashSet)
                    hashSet.remove(nums[i])
                    buildPath.pop()
        
        backtrack(0, set())
        return result 


        