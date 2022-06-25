def rot13(msg):
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    string = ""
    for x in range(0,len(msg)):
        if msg[x].isalpha() == True:
            if msg[x].isupper() == True:
                if alph.index(msg[x].lower())+13 > len(alph)-1:
                    ind = alph.index(msg[x].lower())+13-len(alph)
                    string = string+alph[ind].upper()
                else:
                    ind = alph.index(msg[x].lower())+13
                    string = string+alph[ind].upper()
            else:
                if alph.index(msg[x])+13 > len(alph)-1:
                    ind = alph.index(msg[x])+13-len(alph)
                    string = string+alph[ind]
                else:
                    ind = alph.index(msg[x].lower())+13
                    string = string+alph[ind]
        else:
            string = string+msg[x]
    return string
                
            

