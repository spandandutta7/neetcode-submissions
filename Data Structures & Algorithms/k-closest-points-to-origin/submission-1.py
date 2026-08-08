class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minheap = []

        for coords in points:
            dist = (coords[0]**2 + coords[1]**2, coords)
            minheap.append(dist)
        
        heapq.heapify(minheap)

        output = []
        for i in range(k):
            output.append(heapq.heappop(minheap)[1])
        
        return output


        