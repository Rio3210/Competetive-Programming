class Solution(object):
    def reverseString(self, s:List[str])->None:
        def checker(l,r,string):
            if l>=r:
                return 
            string[l],string[r]=string[r],string[l]
            l+=1
            r-=1
            checker(l,r,string)
        return checker(0,len(s)-1,s)
        
        # a=int(len(s)/2)
        # b=len(s)-1
        # for i in range(0,a):
        #     s[i],s[b]=s[b],s[i]
        #     b-=1
        