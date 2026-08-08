class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = stones

        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            x, y = heapq.heappop_max(max_heap), heapq.heappop_max(max_heap)
            if x != y:
                heapq.heappush_max(max_heap, x - y)
        
        max_heap.append(0)
        return max_heap[0]
            



        