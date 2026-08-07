class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = set()

        for e in nums:
            if e in hashSet:
                return e
            hashSet.add(e)
        