def first_non_repeating_letter(string):
    tuple = {}
    if len(string)>0:
        for x in range(0,len(string)):
            strg = string.lower()
            tuple[strg.count(strg[x])] = string[x]
            if strg.count(strg[x]) == 1:
                return  string[x]
        return ''
    else:
        return string
