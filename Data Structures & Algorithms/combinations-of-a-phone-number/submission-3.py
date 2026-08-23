class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        combos = {2:["a", "b", "c"], 3:["d", "e", "f"], 4:["g", "h", "i"], 5:["j", "k", "l"], 6:["m", "n", "o"], 7:["p", "q", "r", "s"], 8:["t", "u", "v"], 9:["w", "x", "y", "z"]}

        def backtrack(i, running):
            if len(running) == len(digits):
                result.append(running)
                return
            
            for char in combos[int(digits[i])]:
                backtrack(i+1, running + char)
        
        if digits:
            backtrack(0, "")
        
        return result




        