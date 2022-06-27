def order(sentence):
    string = ""
    arr = [" "]+sentence.split()
    arr1 = {}
    for i in range(1,len(arr)):
        for x in range(0,len(arr)):
            if f'{x}' in arr[i]:
                arr1[x] = arr[i]
    for x in range(0,len(arr1)):
        string = string+arr1[x+1]+" "
    return string[:-1]
