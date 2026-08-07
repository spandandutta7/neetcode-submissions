class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()

        for char in s:
            if char not in dict1.keys():
                dict1[char] = 0
            dict1[char] = dict1[char] + 1
        
        for char in t:
            if char not in dict2.keys():
                dict2[char] = 0
            dict2[char] = dict2[char] + 1
        

        return dict1 == dict2