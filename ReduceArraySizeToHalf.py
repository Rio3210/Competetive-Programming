class Solution(object):
    def minSetSize(self, arr):
        n = len(arr)
        count = Counter(arr).most_common()
        count.sort(key=lambda c: -c[1])

        sum = 0
        for i, c in enumerate(count):
          sum += c[1]
          if sum >= n // 2:
            return i + 1
