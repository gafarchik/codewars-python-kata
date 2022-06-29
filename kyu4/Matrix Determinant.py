def determinant(matrix, mul=1):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    sign = -1
    sum = 0
    for x in range(0,width):
        m = [[matrix[j][k] for k in range(width) if k != x] for j in range(1, width)]

        sign *= -1
        sum += mul * determinant(m, sign * matrix[0][x])
    return sum
