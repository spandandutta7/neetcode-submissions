class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        cmax = 0
        hashSet = set()

        while right < len(s):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            

            cmax = max(cmax, (right-left+1))
            hashSet.add(s[right])
            right += 1
        
        return cmax
        