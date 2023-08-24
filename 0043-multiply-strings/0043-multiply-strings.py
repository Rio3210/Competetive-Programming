class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num={"0":0, "1":1,"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        
        numm1=0
        numm2=0
        for i in num1:
            numm1=10 * numm1 + num[i]
        for j in num2:
            numm2 =10* numm2 + num[j]

        return str(numm1 * numm2)