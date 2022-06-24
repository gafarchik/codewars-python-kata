def maskify(cc):
    l = len(cc)
    a=""
    b = cc
    n = ''
    if l >5:
        for x in range(0,l-4):
            a+="#"
        n = '{}{}'.format(a,b[l-4:])
    elif l<5:
        b = cc
        n = '{}{}'.format(a,b)

    return n
