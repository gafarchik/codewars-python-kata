def pig_it(text):
    arr = text.split()
    string = ""
    char = "!?@#$%^&*"
    for x in range(0,len(arr)):
        if arr[x] not in char:
            arr[x] = str(arr[x])[1::]+str(arr[x])[0]+"ay"
    for x in range(0,len(arr)):
        string = string + arr[x] + " "
    return string[:-1:]
