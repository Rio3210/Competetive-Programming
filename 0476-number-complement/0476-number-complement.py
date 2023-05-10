class Solution:
    def findComplement(self, num: int) -> int:
        l=len(bin(num))-2
        gen=int("1"*l,2)
        return gen^num
            