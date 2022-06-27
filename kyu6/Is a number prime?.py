def is_prime(num):
    if num <=1:
        return False
    else:
        for n in range(2,int(num**0.5)+1):
            if num%n==0:
                return False
        return True
