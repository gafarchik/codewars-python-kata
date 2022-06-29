import numpy as np
def delete_nth(order,max_e):
    arr = []
    for x in range(0,len(order)):
        if arr.count(order[x]) >= max_e:
            pass
        else:
            arr.append(order[x])
    return arr
