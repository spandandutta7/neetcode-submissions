class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        discovered = set()
        for num in nums:
            if num in discovered:
                return True
            else:
                discovered.add(num)
        
        return False