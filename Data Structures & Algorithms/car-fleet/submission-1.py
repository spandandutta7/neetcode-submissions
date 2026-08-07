class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        pairs = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort(reverse = True)

        for pos, speed in pairs:
            finishTime = ((target - pos) / speed)
            if not fleets:
                fleets.append(finishTime)
            elif fleets and fleets[-1] < finishTime:
                fleets.append(finishTime)
            
        
        return len(fleets)