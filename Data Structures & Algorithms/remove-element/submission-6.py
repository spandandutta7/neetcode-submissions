class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                if nums[right] == val:
                    right -= 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                    k += 1
            else:
                left += 1
                k += 1
        return k


        