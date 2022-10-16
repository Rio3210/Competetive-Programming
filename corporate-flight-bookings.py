class Solution(object):
    def corpFlightBookings(self, bookings, n):
        
        result = [0] * n
        for first, last, seats in bookings:
            result[first-1] += seats
            if last < n:
                result[last] -= seats
        for i in range(1, n):
            result[i] += result[i-1]
        return result
