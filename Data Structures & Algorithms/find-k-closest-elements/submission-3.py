class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        left, right = 0, k-1
        minDiff = float("inf")
        minValues = [0,0]

        arrD = []
        for e in arr:
            arrD.append(abs(e-x))

        totalDiff = 0  
        while right < len(arr):
            if left == 0:
                for e in arrD[left:right+1]:
                    totalDiff += e
            else:
                totalDiff += arrD[right]
            if totalDiff < minDiff:
                minDiff = totalDiff
                minValues = [left, right]
            totalDiff -= arrD[left]
            left += 1
            right += 1
        
        return arr[minValues[0]:minValues[1]+1]










        