def unique_in_order(iterable):
    arr = []
    for x in range(0,len(iterable)):
        if len(arr)>0:
            if iterable[x]!=arr[-1]:
                arr.append(iterable[x])
        else:
            arr.append(iterable[x])
    return arr
