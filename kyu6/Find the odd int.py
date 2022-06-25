def find_it(seq):
    res = 0
    ans = {}
    for x in range(0,len(seq)):
        if seq[x] not in ans:
            ans[seq[x]] = seq.count(seq[x])
    for x in range(0,len(list(ans.values()))):
        if list(ans.values())[x] % 2 == 0:
            pass
        else:
            res = list(ans)[x]
    return res
