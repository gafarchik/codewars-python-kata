def wave(people):
    res = []
    for x in range(0,len(people)):
        people = people.lower()
        if people[x]!=" ":
            people = people[:x]+people[x].upper()+people[x+1:]
            res.append(people)
    return res
