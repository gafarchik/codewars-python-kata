def sort_array(source_array):
    odd_arr = []
    even_arr = []
    even_pos_list = []
    res = []
    for x in range (0,len(source_array)):
        if source_array[x]%2 == 0:
            even_arr.append(source_array[x])
            even_pos_list.append(x)
        else:
            odd_arr.append(source_array[x])
    odd_arr.sort()
    res = odd_arr
    for x in range(0,len(even_arr)):
        res.insert(even_pos_list[x],even_arr[x])
    return res
