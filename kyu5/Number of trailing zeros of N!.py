def zeros(n):
    p = 5
    count = 0
    while (n / p >= 1):
        count += int(n / p)
        p *= 5

    return int(count)
