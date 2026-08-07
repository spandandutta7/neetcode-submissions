class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        currentMax = 0
        subSet = set()

        while right < len(s):
            while s[right] in subSet:
                subSet.remove(s[left])
                left += 1
            subSet.add(s[right])
            currentMax = max(currentMax, right - left + 1)
            right += 1
        
        return currentMax