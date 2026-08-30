from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        d1, d2 = defaultdict(int), defaultdict(int)
        left, right = 0, len(s1) - 1

        for char in s1:
            d1[char] += 1
        
        for char in s2[left:right+1]:
            d2[char] += 1
        
        while right < len(s2):
            if d1 == d2:
                return True
            
            if right + 1 < len(s2):
                d2[s2[right + 1]] += 1
            
            d2[s2[left]] -= 1
            if d2[s2[left]] == 0:
                del d2[s2[left]]
            
            left, right = left + 1, right + 1
        
        return False