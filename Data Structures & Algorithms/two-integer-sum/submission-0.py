class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftP, rightP = 0, 0

        while leftP < len(nums) - 1:
            rightP = leftP + 1

            while rightP < len(nums):
                if nums[leftP] + nums[rightP] == target:
                    return [leftP, rightP]
                rightP += 1
            
            leftP += 1
                
            
