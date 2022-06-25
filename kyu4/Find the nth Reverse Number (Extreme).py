def find_reverse_number(n):
    if n <= 10:
        return n - 1
    n = str(n)
    if n[0] != '1':
        t = str(int(n[0]) - 1) + n[1:]
        return int(t + t[::-1][1:])
    if n[1] == '0':
        t = str(int(n[0:2]) - 1) + n[2:]
        return int(t + t[::-1][1:])
    else:
        t = str(n)[1:]
        return int(t + t[::-1])
