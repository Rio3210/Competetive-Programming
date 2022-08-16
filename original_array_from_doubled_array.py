class Solution(object):
    def findOriginalArray(self, changed):
        l = []
        q = deque()

        for num in sorted(changed):
            if q and num == q[0]:
                q.popleft()
            else:
                q.append(num * 2)
                l.append(num)

        return [] if q else l

        

                
            
  
        
