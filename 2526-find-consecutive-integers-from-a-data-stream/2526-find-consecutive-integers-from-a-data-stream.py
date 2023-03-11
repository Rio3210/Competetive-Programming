from collections import defaultdict, deque
class DataStream:
    def __init__(self, value: int, k: int):
        self.dq = deque([])
        self.container = defaultdict(int)
        self.length = k
        self.cmp = value
        

    def consec(self, num: int) -> bool:
        if len(self.dq) == self.length:
            pop = self.dq.popleft()
            self.container[pop] -= 1
        self.dq.append(num)
        self.container[num] += 1
        return self.container[self.cmp] == self.length

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)