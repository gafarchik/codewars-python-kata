from math import gcd
def coins(coin1, coin2):
    return coin1 * coin2 - coin1 - coin2 if gcd(coin1, coin2) == 1 else -1
