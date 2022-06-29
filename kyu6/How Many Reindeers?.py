import math
def reindeer(presents):
    if presents > 180:
        raise ValueError('Expected error for 200 presents')
    else:
        return 2+(math.ceil(presents/30))
        
