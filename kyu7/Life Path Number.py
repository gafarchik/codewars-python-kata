def life_path_number(birthdate):
    n = "".join(i for i in birthdate if i.isdigit())
    while len(str(n)) > 1:
        n = sum(i for i in map(int, str(n)))
    return n
