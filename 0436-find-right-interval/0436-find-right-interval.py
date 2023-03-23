class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_points = {}
        
        for i, interval in enumerate(intervals):
            start_points[interval[0]] = i
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        result = [-1] * len(intervals)
        
        for i, interval in enumerate(intervals):
            index = bisect_left(sorted_intervals, [interval[1], -float('inf')])
            if index != len(intervals):
                result[i] = start_points[sorted_intervals[index][0]]
        return result
        
#         output = []
#         maxVal = float("inf")
        
#         for i in range(len(intervals)):
#             smallestStart  = maxVal
#             index = -1
#             for j in range(len(intervals)):
#                 if intervals[j][0] >= intervals[i][1]:
#                     if intervals[j][0] < smallestStart:
#                         smallestStart =  intervals[j][0]
#                         index = j
#             output.append(index)
            
#         return output