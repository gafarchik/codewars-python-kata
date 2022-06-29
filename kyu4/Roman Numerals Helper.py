class RomanNumerals:

    def to_roman(n):
        res = ""
        nums = [(1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),(90, "XC"),(50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"),(4, "IV"),(1, "I"),]
        for cap, roman in nums:
            d, m = divmod(n, cap)
            res += roman * d
            n = m

        return res
    def from_roman(roman):
        nums = {'I':1,'II':2,"III":3,'IV':4,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900,'M':1000}
        i = 0
        res = 0
        while i < len(roman):
            if i+1<len(roman) and roman[i:i+2] in nums:
                res+=nums[roman[i:i+2]]
                i+=2
            else:
                res+=nums[roman[i]]
                i+=1
        return res
