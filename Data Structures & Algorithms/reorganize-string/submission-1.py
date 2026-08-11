class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        maxHeap = []

        for char in s:
            d[char] = d.get(char, 0) + 1
        
        for char, freq in d.items():
            maxHeap.append((freq, char))
        
        heapq.heapify_max(maxHeap)

        result = ""
        prev = None

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""

            count, char = heapq.heappop_max(maxHeap)
            result += char

            if prev:
                heapq.heappush_max(maxHeap, prev)
                prev = None
            
            if count != 1:
                prev = (count-1, char)
        
        return result

            


