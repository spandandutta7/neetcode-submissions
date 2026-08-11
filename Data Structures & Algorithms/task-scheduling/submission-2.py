from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        queue = deque()


        for char in tasks:
            d[char] = d.get(char, 0) + 1
        
        maxHeap = [(cnt, char) for char, cnt in d.items()]
        heapq.heapify_max(maxHeap)

        time = 0
        while maxHeap or queue:
            time += 1
            if not maxHeap and queue:
                time = queue[0][0]
                heapq.heappush_max(maxHeap, queue.popleft()[1])
                continue
            
            count, char = heapq.heappop_max(maxHeap)
            if count - 1 > 0:
                queue.append((time + n, (count - 1, char)))

            if queue and time == queue[0][0]:
                heapq.heappush_max(maxHeap, queue.popleft()[1])
        
        return time



        
        
        