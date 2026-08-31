class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        if len(s2) < len(s1):
            return False
        
        left, right = 0, len(s1)-1
        while right < len(s2):
            if sorted(s2[left:right+1]) == s1:
                return True
            left,right = left+1, right+1
        
        return False



        
        