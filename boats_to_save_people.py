class Solution(object):
    def numRescueBoats(self, people, limit):
        
        
        people.sort()
        l = 0
        r = len(people)-1
        boat = 0
        
        while(l <= r):
            if people[l]+people[r] > limit:
                boat += 1
                r -= 1
            else:
                l += 1
                r -= 1
                
                boat += 1
                
        return boat
        
        
