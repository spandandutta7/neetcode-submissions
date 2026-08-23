class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hashSet = set()
        n = len(board)
        m = len(board[0])



        def backtrack(row, col, i):
            if i == len(word):
                return True
            if row >= n or col >= m or (row, col) in hashSet or word[i] != board[row][col] or min(row, col) < 0:
                return False
            

            hashSet.add((row, col))
            result = backtrack(row, col + 1, i+1) or backtrack(row, col - 1, i+1) or backtrack(row+1, col, i+1) or backtrack(row-1, col, i+1)
            
            hashSet.remove((row, col))
            return result


        for r in range(n):
            for c in range(m):
                if backtrack(r, c, 0):
                    return True

        return False

            

        