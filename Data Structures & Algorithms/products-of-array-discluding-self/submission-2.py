class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix, result  = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result


        