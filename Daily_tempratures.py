class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            
            
            if stack and T[i] < T[stack[-1]]:
                ans[i] = stack[-1] - i
            stack.append(i)

        return ans
