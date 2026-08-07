class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        used = False

        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[left+1:right+1]) or self.isPalindrome(s[left:right])
            right -= 1
            left += 1
        
        return True
    
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            right -= 1
            left += 1

        return True