def in_array(arr1, arr2):
    arr = []
    for x in range(0,len(arr1)):
        for y in range(0,len(arr2)):
            if arr1[x] in arr2[y]:
                if arr1[x] not in arr:
                    arr.append(arr1[x])
    arr.sort()
    return arr
