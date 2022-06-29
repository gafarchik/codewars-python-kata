def count(string):
    count_tpl = {}
    for x in range(0,len(string)):
        count_tpl[string[x]] = string.count(string[x])
    return count_tpl
