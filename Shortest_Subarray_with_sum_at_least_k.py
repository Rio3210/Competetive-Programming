class Solution(object):
    def shortestSubarray(self, array, k):
        queue = []
        prefixSums = [0 ]*(len(array)+1)
        for i in range(len(array)):
            prefixSums[i + 1] = prefixSums[i] + array[i]

        shortestSum = len(array)+1

        for y in range(len(prefixSums)):
            while(len(queue) > 0 and prefixSums[y] <= prefixSums[queue[-1]]):
                queue.pop()

            while(len(queue) > 0 and prefixSums[y] >= prefixSums[queue[0]] + k):
                shortestSum = min(shortestSum, y - queue.pop(0))

            queue.append(y)

        return shortestSum if shortestSum < len(array)+1 else -1
