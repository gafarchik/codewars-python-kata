def sum_array(arr):
    if arr != None:
        if arr != []:
            arr.remove(max(arr))
            if len(arr) >=1:
                arr.remove(min(arr))
            return sum(arr)
        else:
            return 0
    else:
        return 0
