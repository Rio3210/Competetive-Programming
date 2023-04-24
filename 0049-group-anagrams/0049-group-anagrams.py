class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt=defaultdict(list)
        for i in strs:
            dictt[''.join(sorted(i))].append(i)
        return dictt.values()