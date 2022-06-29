def tower_builder(n_floors):
    return [('*'*(n*2-1)).center(n_floors*2-1) for n in range(1, n_floors+1)]
