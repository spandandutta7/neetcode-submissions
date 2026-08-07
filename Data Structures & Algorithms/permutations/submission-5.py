class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        hashSet = set()
        

        def dfs(result, hashSet, buildPath):
            if len(hashSet) == len(nums):
                result.append(buildPath.copy())
                return

            for num in nums:
                if num not in hashSet:
                    hashSet.add(num)
                    buildPath.append(num)
                    dfs(result, hashSet, buildPath)

                    buildPath.pop()
                    hashSet.remove(num)
        
        dfs(result, hashSet, [])
        return result


        