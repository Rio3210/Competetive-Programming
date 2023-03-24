class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leader = []
        votes = defaultdict(int)
        winner = -1
        for p in persons:
            votes[p] += 1
            if votes[p] >= votes[winner]:
                winner = p
            self.leader.append(winner)

    def q(self, t: int) -> int:
        # l, r = 0, len(self.times)
        # while l<r:
        #     m = l+(r-l)//2
        #     if t < self.times[m]:
        #         r = m
        #     else:
        #         l = m+1
        idx=bisect_right(self.times,t)-1
        return self.leader[idx]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)