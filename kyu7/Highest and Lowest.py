def high_and_low(numbers):
    numbers = numbers.split(" ")
    numbers = list(map(int, numbers))
    return '{} {}'.format(max(numbers), min(numbers))
