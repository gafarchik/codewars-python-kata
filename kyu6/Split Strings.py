def solution(s):
    arr = []
    if len(s) > 0:
        if len(s)%2 == 0:
            for x in range(0,len(s),2):
                arr.append(s[x:x+2])
        else:
            s = s+"_"
            for x in range(0,len(s),2):
                arr.append(s[x:x+2])
    return arr
