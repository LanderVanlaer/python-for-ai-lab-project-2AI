def r_get_all_possibilities(n_layers, values):
    if n_layers == 1:
        return [[a] for a in values]

    possibilities = []

    for a in values:
        for others in r_get_all_possibilities(n_layers - 1, values):
            possibilities.append([a, *others])

    return possibilities

def r_get_all_combinations(n_layers, values):
    if len(values) == 1:
        return [[row] for row in r_get_all_possibilities(n_layers, values[0])]
    lst = []

    for row in r_get_all_possibilities(n_layers, values[0]):
        for row2 in r_get_all_combinations(n_layers, values[1:]):
            lst.append([row, *row2])
        
    return lst