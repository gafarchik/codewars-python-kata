def alphabet_position(text):
    alpha = ["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    string = ""
    
    for x in range(0,len(text)):
        if text.lower()[x].isalpha()==True:
            string = string + str(alpha.index(text.lower()[x])) + " "
    return string[:-1]
