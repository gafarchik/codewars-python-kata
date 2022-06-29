def solution(roman):
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
