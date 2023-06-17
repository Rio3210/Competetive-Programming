class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wor=Counter(words)
        
        ans=sorted(wor.items(),key=lambda x: (-x[1],x[0]))

        final=[]
        for i in range(k):
            final.append(ans[i][0])
        return final
        
        
        
        