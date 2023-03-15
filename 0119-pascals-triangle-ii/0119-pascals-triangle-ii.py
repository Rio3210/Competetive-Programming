class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        prev_row = self.getRow(rowIndex - 1)
        new_row = [1] * (len(prev_row) + 1)
        for i in range(1, len(new_row)-1):
            new_row[i] = prev_row[i-1] + prev_row[i]
        return new_row