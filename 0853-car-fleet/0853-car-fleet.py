class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=0
        cars = sorted(zip(position, speed), reverse=True)
        times = [float(target - p) / s for p, s in cars]
        print(times)
        maxTime = 0  

        for time in times:
              if time > maxTime:
                maxTime = time
                res += 1
        return res