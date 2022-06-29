def valid_braces(string):
    type_braces = ['()', '{}', '[]']
    while any(x in string for x in type_braces):
        for brace in type_braces:
            string = string.replace(brace, '')
    return not string
        
