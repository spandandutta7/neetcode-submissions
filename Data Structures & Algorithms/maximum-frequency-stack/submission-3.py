class FreqStack:

    def __init__(self):
        self.d = {}
        self.maxheap = []
        self.order = 0
        
        

    def push(self, val: int) -> None:
        self.d[val] = self.d.get(val, 0) + 1
        heapq.heappush_max(self.maxheap, (self.d[val], self.order, val))
        self.order += 1


    def pop(self) -> int:
        tup = heapq.heappop_max(self.maxheap)
        self.d[tup[2]] = self.d.get(tup[2], 0) - 1
        return tup[2]
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()