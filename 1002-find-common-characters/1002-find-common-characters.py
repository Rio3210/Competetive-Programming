class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = collections.Counter(words[0])
        for string in words:
            new_count = collections.Counter(string)
            for k in count:
                count[k] = min(count[k], new_count[k])
        print(count)
        return count.elements()        