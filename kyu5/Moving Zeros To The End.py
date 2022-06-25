def move_zeros(array):
    count = 0
    arr = []
    for x in range(0,len(array)):
        if array[x] != 0:
            arr.append(array[x])
        else:
            count+=1
    for x in range(0,count):
        arr.append(0)
    array=arr
    return array
