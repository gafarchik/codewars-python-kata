import numpy as np
def find_uniq(arr):
    nparr = np.array(arr)
    values, counts = np.unique(arr, return_counts=True)
    npdict = dict(zip(counts, values))
    return npdict[1]

