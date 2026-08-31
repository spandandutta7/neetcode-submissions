class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for ind in range(len(nums)):
            if nums[ind] in d and abs(d[nums[ind]] - ind) <= k:
                return True
            d[nums[ind]] = ind
        
        return False





        