class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        res=high
        while low<=high:
            acc=low+(high-low)//2
            day = sums =0
            for i in range(len(weights)):
                sums += weights[i]
                if sums>acc:
                    day+=1
                    sums=weights[i]
                elif sums==acc:
                    day+=1
                    sums=0
            if sums:
                day+=1     
            if day<=days:
                high=acc-1
            else:
                low=acc+1
        return low
            