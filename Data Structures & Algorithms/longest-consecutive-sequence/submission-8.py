class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        longest = 0
        current = 0

        for i, e in enumerate(nums):
            if i == 0:
                current = 1
                continue
            if e == nums[i-1] + 1:
                current += 1
            elif e == nums[i-1]:
                continue
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)


        