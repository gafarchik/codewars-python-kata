def sum_triangular_numbers(n):
    if n <= 0:
        return 0

    sum = sum_triangular_numbers(n-1)
    return sum + (n * (n + 1)) / 2
