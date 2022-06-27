def duplicate_encode(word):
    string = ""
    for x in range(0,len(word)):
        if word.lower().count(word.lower()[x]) == 1:
            string = string+"("
        else:
            string = string+")"
    return string
