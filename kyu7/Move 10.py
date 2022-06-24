def move_ten(st):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    l = len(st)
    a = len(alphabet)
    true = ""
    if l > 0:
        for x in range(0,l):
            check=st[x]
            ind = alphabet.index(check)
            if ind+11 > a:
                r = ind+10
                r = r-a
                true+=alphabet[r]
            else:
                true+=alphabet[ind+10]
    return true
