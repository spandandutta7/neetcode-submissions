class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        buildPath = []
        nums = sorted(nums)

        def backtrack(index):
            if index == len(nums):
                result.append(buildPath[::])
                return
            
            buildPath.append(nums[index])
            backtrack(index+1)
            buildPath.pop()

            i = index
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i +=1
            
            backtrack(i+1)
            

            


            

        backtrack(0)
        return result