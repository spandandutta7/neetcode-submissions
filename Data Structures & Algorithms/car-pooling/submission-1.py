class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = defaultdict(int)

        for numP, start, end in trips:
            d[start] += numP
            d[end] -= numP
        
        runningC = 0
        for key in sorted(d.keys()):
            runningC += d[key]
            if runningC > capacity:
                return False

        return True
        