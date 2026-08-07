class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        buildPath = []

        def backtrack(start):

            if len(buildPath) == k:
                result.append(buildPath.copy())
                return
            
            for i in range(start, n+1):
                buildPath.append(i)
                backtrack(i+1)
                buildPath.pop()


        backtrack(1)
        return result


        