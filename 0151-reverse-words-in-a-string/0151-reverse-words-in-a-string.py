class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()[::-1]
        # print(w)
        return ' '.join(w)