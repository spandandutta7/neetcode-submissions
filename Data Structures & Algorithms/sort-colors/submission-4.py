class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = defaultdict(int)

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        nums[:] = [0] * d[0] + [1] * d[1] + [2] * d[2]


        