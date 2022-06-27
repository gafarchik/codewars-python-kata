def positive_sum(arr):
    array = []
    for x in range(0,len(arr)):
        if arr[x] > 0:
            array.append(arr[x])
    return sum(array)

