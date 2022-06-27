def find_missing_letter(chars):
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if len(chars)>0:
        first_elem = alpha.index(chars[0].lower())
        for x in range(0,len(chars)):
            if chars[x].lower() != alpha[first_elem]:
                return alpha[first_elem].upper() if chars[x].isupper() == True else alpha[first_elem]
            first_elem+=1
    return chars

