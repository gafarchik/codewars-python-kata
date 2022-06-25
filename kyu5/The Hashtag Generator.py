def generate_hashtag(s):
    if len(s)>140:
        s = False
    elif len(s)>0:
        arr = s.split()
        s = "#"
        for x in range(0,len(arr)):
            arr[x] = str(arr[x])[0].upper()+str(arr[x])[1::].lower()
            s = s+arr[x]
    else:
        s = False
    return s
