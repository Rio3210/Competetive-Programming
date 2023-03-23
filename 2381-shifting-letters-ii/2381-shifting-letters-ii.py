class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:        
        n=len(s)
        move_map=[0]*(n+1)
        for start,end,direction in shifts:
            if direction==1:
                move_map[start]+=1
                move_map[end+1]-=1
            else:
                move_map[start]-=1 
                move_map[end+1]+=1
        print(move_map)
        for i in range(1,n):
            move_map[i]+=move_map[i-1]
        
        ans=[]
        orda=ord('a')
        for i,c in enumerate(s):
            current=(ord(c)-orda+move_map[i])%26
            ans.append(chr(current+orda))  
        return ''.join(ans)