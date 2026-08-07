class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        currMax = 0

        while left < right:
            
            area = (right - left) * (min(heights[right], heights[left]))

            currMax = max(currMax, area)

            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        

        return currMax