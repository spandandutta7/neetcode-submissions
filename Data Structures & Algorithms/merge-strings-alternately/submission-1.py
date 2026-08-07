class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(min(len(word1), len(word2))):
            result += word1[0]
            result += word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        
        result += word1
        result += word2
        return result

        