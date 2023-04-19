class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        stack=[]
        n=len(matrix)
        for i in range(n):
            stack=stack + matrix[i]
        stack.sort()
        print(stack)
        return stack[k-1]