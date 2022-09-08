class Solution(object):
    def maxResult(self, nums, k):
        dq, n = deque([len(nums)-1]), len(nums)        
        for i in range(n-2, -1, -1):
            while dq and dq[0] > i + k:
                dq.popleft()
            nums[i] += nums[dq[0]]
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        return nums[0]
