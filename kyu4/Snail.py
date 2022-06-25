def get(data):
    ln = len(data)
    if ln == 1:
        return data[0]
    first_line = data[0]
    second_line = []
    if ln >= 3:
        for i in range(1,ln-1):
            second_line.append(data[i][ln-1])
    third_line = data[ln-1]
    third_line.reverse()
    fourth_line = []
    if ln >= 3:
        for j in range(1,ln-1):
            fourth_line.append(data[j][0])
    fourth_line.reverse()
    return first_line + second_line + third_line + fourth_line
    
def cut(data):
    ln = len(data)
    nw = []
    for i in range(1,ln-1):
        nw.append(data[i][1:ln-1])
    return nw

def snail(snail_map):
    res = []
    while len(snail_map) >= 3:
        res = res + get(snail_map)
        snail_map = cut(snail_map)
    res = res + get(snail_map)
    return res
