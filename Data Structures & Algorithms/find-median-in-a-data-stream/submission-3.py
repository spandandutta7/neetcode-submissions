class MedianFinder:

    def __init__(self):
        self.leftSide = []
        self.rightSide = []
        

    def addNum(self, num: int) -> None:
        
        if not self.leftSide or self.leftSide[0] >= num:
            heapq.heappush_max(self.leftSide, num)
        else:
            heapq.heappush(self.rightSide, num)
        
        if abs(len(self.rightSide)-len(self.leftSide)) > 1:
            if len(self.rightSide)>len(self.leftSide):
                heapq.heappush_max(self.leftSide, heapq.heappop(self.rightSide))
            else:
                heapq.heappush(self.rightSide, heapq.heappop_max(self.leftSide))

        

    def findMedian(self) -> float:
        if len(self.leftSide) == len(self.rightSide):
            return (self.leftSide[0] + self.rightSide[0]) / 2
        elif len(self.leftSide) > len(self.rightSide):
            return self.leftSide[0]
        else:
            return self.rightSide[0]
        
        