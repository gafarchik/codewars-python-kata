def difference_of_squares(n):
    r = range(1,n+1,1)
    return (sum(r) ** 2) - (sum( z**2 for z in r))
