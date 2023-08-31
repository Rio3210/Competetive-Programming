class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        st=[0]
        n=len(s)
        for i in range(n):
            
            for j in st:
                if s[j:i+1] in wordDict:
                    st.append(i+1)
                    break
        if len(s)==st[-1]:
            return True
        else:
            return False
            