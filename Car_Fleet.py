class Solution(object):
    def carFleet(self, target, position, speed):
        ans = 0
        times = [
            float(target - p) / s for p, s in sorted(zip(position, speed),
                                                     reverse=True)]
        maxTime = 0 

        for time in times:
          
          if time > maxTime:
            maxTime = time
            ans += 1

        return ans
