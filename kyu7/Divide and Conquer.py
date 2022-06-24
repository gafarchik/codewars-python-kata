def div_con(x):
    # your code here
    number = []
    string = []
    for y in range(0,len(x)):
        check=x[y]
        t = type(check)
        if t is int:
            number.append(check)
        if t is str:
            p = int(check)
            string.append(int(check))
    result = sum(number)-sum(string)
    print(result)
    return result
