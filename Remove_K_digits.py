class Solution(object):
    def removeKdigits(self, num, k):
        stack=[]
        for elt in num:
            while k>0 and stack and stack[-1]>elt:
                k-=1
                stack.pop()
            stack.append(elt)
        stack=stack[:len(stack)-k]
        res="".join(stack)
        return str(int(res)) if res else "0"
