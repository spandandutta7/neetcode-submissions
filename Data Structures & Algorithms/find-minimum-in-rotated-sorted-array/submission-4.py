class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        result = nums[0]

        while left <= right:
            mid = left + ((right-left)//2)

            if nums[right] > nums[left]:
                result = min(result, nums[left])
                break

            result = min(result, nums[mid])
            if nums[right] >= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return result
            