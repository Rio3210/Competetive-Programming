class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s1)>len(s2):
        #     return False
        # m,n = len(s1) , len(s2)
        # c1=Counter(s1)
        # c2=Counter(s2[:m])
        # for i in range(n-m+1):
        #     c2
        #     if c1==c2:
        #         return True 
        # return False
        
        sn = len(s1)
        pn= len(s2)
        dict_p =Counter(s1)
        for i in range(pn-sn+1):
            dict_s =Counter(s2[i : sn+i])
            if dict_s == dict_p:
                return True
        return False