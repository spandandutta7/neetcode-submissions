class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        hashSet = set()
        res = []

        def backtrack(nums, buildPath, hashSet, res):
            if len(nums) == len(buildPath):
                res.append(buildPath[:])
                return
            for num in nums:
                if num not in hashSet:
                    hashSet.add(num)
                    buildPath.append(num)
                
                    backtrack(nums, buildPath, hashSet, res)

                    buildPath.pop()
                    hashSet.remove(num)
        
        backtrack(nums, [], hashSet, res)
        return res




