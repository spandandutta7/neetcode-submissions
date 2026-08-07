class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            sorteD = tuple(sorted(word))
            if sorteD in d.keys():
                d[sorteD].append(word)
            else:
                d[sorteD] = [word]
        
        result = []
        for elem in d.values():
            result.append(elem)
        
        return result