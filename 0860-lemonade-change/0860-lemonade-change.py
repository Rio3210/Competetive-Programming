class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_five = 0
        count_ten = 0
        for bill in bills:
            if bill == 5:
                count_five += 1
            elif bill == 10:
                if count_five < 1:
                    return False
                count_five -= 1
                count_ten += 1
            else:
                if count_five > 0 and count_ten > 0:
                    count_five -= 1
                    count_ten -= 1
                elif count_five >= 3:
                    count_five -= 3
                else:
                    return False
        return True