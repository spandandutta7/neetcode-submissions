class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = []
        availableTasks = []
        tasksLeft = []


        for index, task in enumerate(tasks):
            tasksLeft.append((task[0], task[1], index))
        heapq.heapify(tasksLeft)

        time = 0
        while tasksLeft or availableTasks:
            while tasksLeft and tasksLeft[0][0] <= time:
                enqueueTime, processingTime, ind = heapq.heappop(tasksLeft)
                heapq.heappush(availableTasks, (processingTime, ind))
            

            if not availableTasks:
                time = tasksLeft[0][0]
                continue
            
            pt, ind = heapq.heappop(availableTasks)
            time += pt
            result.append(ind)

        return result




            
            



        