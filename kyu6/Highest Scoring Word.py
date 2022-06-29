def high(x):
    arr = x.split()
    val = []
    score = 0
    alpha = ["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for x in range(0,len(arr)):
        score = 0
        for i in range(0,len(arr[x])):
            score = score+alpha.index(arr[x][i])
        val.append(score)
    return arr[val.index(max(val))]
