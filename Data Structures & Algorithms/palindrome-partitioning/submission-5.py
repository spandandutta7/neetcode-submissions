class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(i, currentPath):
            if i >= len(s):
                result.append(currentPath.copy())
            for j in range(i, len(s)):
                if isPali(self, s, i, j):
                    currentPath.append(s[i:j+1])
                    dfs(j+1, currentPath)
                    currentPath.pop()


        def isPali(self, s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        dfs(0, [])
        return result


        


        
        