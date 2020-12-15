class Solution:
    def romanToInt(self, s: str):
        romandict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        romandict1 = {"IV": 2, "IX": 2, "XL": 20, "XC": 20, "CD": 200, "CM": 200}
        sum = 0
        for i in s:
            sum = sum + romandict[i]

        for i in romandict1:
            if i in s:
                sum = sum - romandict1[i]

        return sum
