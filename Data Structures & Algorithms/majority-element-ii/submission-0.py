class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = {}

        for e in nums:
            hashMap[e] = hashMap.get(e, 0) + 1
        
        res = []
        for e, freq in hashMap.items():
            if freq > len(nums)/3:
                res.append(e)
        
        return res

        


        