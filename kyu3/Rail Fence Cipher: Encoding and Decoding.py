def encode_rail_fence_cipher(string, n):
    encode = {}
    row = 1
    back = 0
    res = ""
    ans = ""
    for x in range(1,n+1):
        encode[x] = ""
    for x in range(0,len(string)):
        if back == 0:
            if row >=n+1:
                row = n-1
                back = 1
            else:
                pass
        encode[row] = encode[row] + string[x]
        if back == 1:
            if row <=1:
                back = 0
                row = 2
            else:
                row -=1
        else:
            row+=1
    for x in range(1,n+1):
        res = res+encode[x]
    print(encode)
    return res
def decode_rail_fence_cipher(string, n):
    encode = {}
    row = 1
    back = 0
    res = ""
    ans = ""
    strg = string
    decode = {}
    decodearr = {}
    for x in range(1,n+1):
        encode[x] = ""
        decode[x]=""
        decodearr[x] = ""
    for x in range(0,len(string)):
        if back == 0:
            if row >=n+1:
                row = n-1
                back = 1
            else:
                pass
        encode[row] = encode[row] + string[x]
        if back == 1:
            if row <=1:
                back = 0
                row = 2
            else:
                row -=1
        else:
            row+=1
    for x in range(1,n+1):
        res = res+encode[x]
    for x in range(1,n+1):
        if len(res) !=0:
            decode[x]=strg[:len(encode[x])]
            strg = strg[len(encode[x]):]
    row = 1
    for x in range(0,len(string)+10):
        if back == 0:
            if row >=n+1:
                row = n-1
                back = 1
            else:
                pass
        if len(decode[row])>0: 
            decodearr[row] = decodearr[row] + decode[row][0]
            decode[row] = decode[row][1:]
            ans = ans+decodearr[row][0]
            decodearr[row] = decodearr[row][1:]
        else:
            pass
        if back == 1:
            if row <=1:
                back = 0
                row = 2
            else:
                row -=1
        else:
            row+=1
    return ans
