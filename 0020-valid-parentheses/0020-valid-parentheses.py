class Solution(object):
    def isValid(self, s):
        stack=[]
        opening=['(','{','[']
        closing=[')','}',']']
        
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                ind=closing.index(i)
                if (len(stack)>0 and (opening[ind]== stack[len(stack)-1])):
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        """
        :type s: str
        :rtype: bool
        """
        