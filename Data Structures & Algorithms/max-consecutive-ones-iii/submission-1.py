class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left, res = 0, -1
        zeroCount = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > k and left <= right:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            res = max(res, right-left+1)
        
        return res
            




        