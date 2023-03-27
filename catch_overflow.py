import sys
import math
import collections
import itertools

MOD = 1000000007
mx = pow(2, 32) - 1

def solve():
    n = int(input())
    stack = [1]
    total = 0
    overflow = False
    for i in range(n):
        s = input().split()
        if s[0] == 'for':
            num = stack[-1]
            if num == -1:
                stack.append(-1)
            elif num * int(s[1]) > mx:
                stack.append(-1)
            else:
                stack.append(num * int(s[1]))
        elif overflow == False:
            if s[0] == 'add':
                if stack[-1] != -1:
                    total += stack[-1]
                else:
                    overflow = True
            elif s[0] == 'end':
                stack.pop()
        if total > mx:
            overflow = True
    if not overflow:
        print(total)
    else:
        print("OVERFLOW!!!")

if __name__ == '__main__':
    #FAST_IO()
    t = 1
    #t = int(input())
    for _ in range(t):
        solve()
