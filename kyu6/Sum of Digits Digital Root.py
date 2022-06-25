def digital_root(n):
    ans = 10
    res = 0
    while len(str(ans)) != 1:
        if len(str(n)) > 1:
            res = 0
            for x in range(0,len(str(n))):
                res = res+int(str(n)[x])
            n = res
        else:
            ans = n
    return ans 
