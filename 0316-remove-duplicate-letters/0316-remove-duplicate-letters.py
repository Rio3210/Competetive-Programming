class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        cnt= Counter(s)
        stack=[]
        
        for ch in s:          
            if ch in stack:
                cnt[ch]-=1
                continue
            while stack and stack[-1]>ch and cnt[stack[-1]]>0:
                stack.pop()
            cnt[ch]-=1
            stack.append(ch)
        return "".join(stack)
        