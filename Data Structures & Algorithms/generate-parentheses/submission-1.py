class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(buildPath, openCount, closeCount):
                if openCount + closeCount == (2*n):
                    result.append(buildPath)
                    return
                
                if openCount < n:
                    dfs(buildPath + "(", openCount + 1, closeCount)

                if closeCount < openCount:
                    dfs(buildPath + ")", openCount, closeCount + 1)
        
        dfs("", 0, 0)
        return result
            


            


            
