class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set(s)
        res = -1

        for char in charset:
            left, charCount = 0, 0
            for right in range(len(s)):
                if s[right] == char:
                    charCount += 1
                
                while right-left+1 - charCount > k:
                    if s[left] == char:
                        charCount -= 1
                    left += 1
                res = max(res, right - left + 1)
        
        return res

            



        