def valid_parentheses(string):
    val = True
    alph = ["q","w","e","r","t","y","u","i","o","p","[","]","\\","a","s","d","f","g","h","j","k","l",";","'","z","x","c","v","b","n","m",",",".","/","?","<",">","|","1","2","3","4","5","6","7","8","9","0"]
    for x in range(0,len(alph)):
        string = string.replace(alph[x],"")
    for x in range(0,len(string)):
        if "()" in string:
            string = string.replace("()","")
    if "(" in string:
        val = False
    elif ")" in string:
        val = False
    elif "()" in string:
        valid_parentheses(string)
    else:
        val=True
    
    return val
