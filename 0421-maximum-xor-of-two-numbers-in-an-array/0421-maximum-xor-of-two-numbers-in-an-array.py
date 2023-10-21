class Trie:

    def __init__(self, leng):
        self.dic = dict()
        self.leng = leng


    def add(self, digit):
        b = bin(digit)[2:]
        b = [int(v) for v in b]
        
        s = [0] * self.leng
        s = (self.leng - len(b)) * [0] + b
        
        xor = ''
        cur = self.dic
        xor_cur = self.dic
        for v in s:
            op_bit = 1 - v
            if v not in cur:
                cur[v] = {}

            cur = cur[v]
            if op_bit in xor_cur:
                xor += '1'
                xor_cur = xor_cur[op_bit]
            else:
                xor += '0'
                xor_cur = xor_cur[v]
        return xor
            

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        l = len(bin(max(nums))[2:])
        trie = Trie(l)

        max_xor = 0
        for v in nums:
            xor = trie.add(v)
            max_xor = max(max_xor, int(xor, 2))

        return max_xor