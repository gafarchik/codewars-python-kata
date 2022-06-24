def powers_of_two(n):
    list = [1]
    for x in range(0,n):
        if len(list)==1:
            list.append(2)
        else:
            list.append(list[-1]*2)
    return list
