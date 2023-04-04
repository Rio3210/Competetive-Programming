class Solution:
    def partitionString(self, s: str) -> int:
        count=0
        container={}
        n=len(s)
        for j in range(n):
            if s[j] in container:
                container={}
                count+=1
                container[s[j]]=j
            else:
                container[s[j]]=j
        if len(container)!=0:
            count+=1
        return count
                