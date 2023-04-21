class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        ans=[]
        for i in s:
            temp=ord(i)
            if temp >= 65 and temp <= 90: 
                ans.append(chr(temp+32))
            else:
                ans.append(chr(temp))
        # print(ans)
        return "".join(ans)