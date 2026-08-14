class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        maxHeap = []
        result = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        for num, freq in d.items():
            result[freq].append(num)
        
        res = []

        for freq in range(len(result)-1, 0, -1):
            for item in result[freq]:
                res.append(item)
                if len(res) == k:
                    return res
        
        return []


        

        


        