class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = [(count, char) for count, char in [(a, "a"), (b, "b"), (c, "c")] if count != 0]
        heapq.heapify_max(maxHeap)
        res = ""

        while maxHeap:
            count, char = heapq.heappop_max(maxHeap)
            if len(res) > 1 and (res[-1] == res[-2] == char):
                if maxHeap:
                    count2, char2, = heapq.heappop_max(maxHeap)
                    res += char2
                    if count2 != 1:
                        heapq.heappush_max(maxHeap, (count2-1, char2))
                    heapq.heappush_max(maxHeap, (count, char))
                else:
                    break

            else:
                res += char
                if count != 1:
                    heapq.heappush_max(maxHeap, (count-1, char))
        return res

        