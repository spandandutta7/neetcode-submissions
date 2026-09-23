class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        minV, maxV = [], []
        left, res = 0, -1

        for right, val in enumerate(nums):
            heapq.heappush(minV, (val, right))
            heapq.heappush_max(maxV, (val, right))

            while abs(minV[0][0] - maxV[0][0]) > limit:
                left += 1
                while minV and minV[0][1] < left:
                    heapq.heappop(minV)
                while maxV and maxV[0][1] < left:
                    heapq.heappop_max(maxV)
            
            res = max(res, right-left+1)    
        
        return res







        