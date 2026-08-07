class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for e in nums:
            if e not in freqDict.keys():
                freqDict[e] = 0
            freqDict[e] = freqDict[e] + 1
        

        bucketList = [[] for i in range(len(nums) + 1)]


        for item, count in freqDict.items():
            bucketList[count].append(item)
        
        result = []
        for i in range(len(bucketList) - 1, 0, -1):
            for e in bucketList[i]:
                result.append(e)
            
            if len(result) == k:
                return result