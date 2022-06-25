def find_missing(sequence):
    a1 =sequence[0]
    a2 =sequence[1]
    a3 =sequence[2]
    d = a2-a1
    a = a1
    ans = 0
    arr = []
    x = 0
    if d == a3-a2:
        d = d
    else:
        d = a3-a2
    while ans == 0:
        arr.append(a)
        if sequence[x]!=arr[x]:
            ans = arr[x]
            break
        else:
            x+=1
            a = a+d
    return ans 
find_missing([1, 3, 4, 5, 6, 7, 8, 9])
