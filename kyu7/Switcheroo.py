def switcheroo(string):
    trueword=""
    for x in range (0,len(string)):
        check = string[x]
        if check == "a":
            trueword+="b"
        elif check == "b":
            trueword+="a"
        elif check == "c":
            trueword+="c"
    return trueword
