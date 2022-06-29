def expanded_form(num):
    arr = []
    string = f'{num}'
    res = ""
    for x in range(0,len(string)):
        arr.append(string[x])
    for x in range(0,len(arr)):
        if arr[x]!="0":
            zero = "0"*(int(len(arr)-x)-1)
            res = res + arr[x]+zero+" + "
    return res[:-3]
