class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        int_to_word = {
            1000000000: "Billion",
            1000000: "Million",
            1000: "Thousand",
            100: "Hundred",
            90: "Ninety",
            80: "Eighty",
            70: "Seventy",
            60: "Sixty",
            50: "Fifty",
            40: "Forty",
            30: "Thirty",
            20: "Twenty",
            19: "Nineteen",
            18: "Eighteen",
            17: "Seventeen",
            16: "Sixteen",
            15: "Fifteen",
            14: "Fourteen",
            13: "Thirteen",
            12: "Twelve",
            11: "Eleven",
            10: "Ten",
            9: "Nine",
            8: "Eight",
            7: "Seven",
            6: "Six",
            5: "Five",
            4: "Four",
            3: "Three",
            2: "Two",
            1: "One",
        }
        
        sorted_keys = [
            1000000000,
            1000000,
            1000,
            100,
            90,
            80,
            70,
            60,
            50,
            40,
            30,
            20,
            19,
            18,
            17,
            16,
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1
        ]
        
        result = ""
        for key in sorted_keys:
            quotient = num // key
            if 0 < quotient < 10:
                if num >= 100:
                    result += int_to_word[quotient] + " " 
                result += int_to_word[key] + " "
            elif quotient >= 10:
                quotient_result = self.numberToWords(quotient)
                result += quotient_result + " " + int_to_word[key] + " "
            num -= quotient * key
        return result.strip()
