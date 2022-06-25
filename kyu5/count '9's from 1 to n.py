def count_nines(n):
    count = 0
    number = [i for i in f'{n}']

    while len(number) > 0:
        if len(number) == 1:
            if number[0] == '9':
                count = count+1
        else:
            count = count + int(number[0]) * int(f'{len(number)-1}' + '0' * (len(number)-2))
            if number[0] == '9':
                count = count + int(''.join(number[1:]))+1
        number.pop(0)

    return count
