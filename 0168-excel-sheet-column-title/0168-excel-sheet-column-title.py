class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            remainder = columnNumber % 26
            if remainder == 0:
                title += 'Z'
                columnNumber -= 1
            else:
                title += chr(ord('A') + remainder - 1)
            columnNumber //= 26
        return title[::-1]
