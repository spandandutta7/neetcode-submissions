class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result = []
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        def sort_func(x):
            return (d[x], -x)
        
        for val in sorted(d.keys(), key = sort_func):
            result.extend([val] * d[val])
        
        return result