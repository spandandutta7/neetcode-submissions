class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        result = [intervals[0]]

        for inter in intervals:
            if inter == intervals[0]:
                continue
            if inter[0] <= result[-1][-1]:
                result[-1][-1] = max(inter[1], result[-1][-1])
            else:
                result.append(inter)
        
        return result


        