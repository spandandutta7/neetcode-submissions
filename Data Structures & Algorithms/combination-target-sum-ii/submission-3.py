class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        buildPath = []
        candidates.sort()

        def backtrack(start):
            if sum(buildPath) == target:
                result.append(buildPath.copy())
                return
            if sum(buildPath) > target or start == len(candidates):
                return


            #Include and continue
            buildPath.append(candidates[start])
            backtrack(start+1)
            buildPath.pop()

            i = start
            #Exclude and continue + handling duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return result


        