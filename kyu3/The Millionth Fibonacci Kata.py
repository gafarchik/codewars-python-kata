def sumfunc(num1, num2, num3, num4, n):
    if n == 0:
        return num2
    if n % 2 == 0:
        return sumfunc(num1, num2, num3 * num3 + num4 * num4, num4 * num4 + 2 * num3 * num4, n / 2)
    else:
        return sumfunc(num2 * num4 + num1 * num4 + num1 * num3, num2 * num3 + num1 * num4, num3, num4, n - 1)

def fib(n):
    if n <= 0:
        num, num2 = 1,0
        for x in range(0, n, -1):
            num2, num = num - num2, num2
        return num2
    if n > 0:
        return sumfunc(1, 0, 0, 1, n)
