class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        maxHeap = []
        reslt = []

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        for num, freq in d.items():
            heapq.heappush_max(maxHeap, (freq, num))
        
        for i in range(k):
            reslt.append(heapq.heappop_max(maxHeap)[1])
        
        return reslt

        

        


        