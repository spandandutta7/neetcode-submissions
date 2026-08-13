class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for string in strs:
            sortD = tuple(sorted(string))
            d[sortD].append(string)
        

        return list(d.values())




        