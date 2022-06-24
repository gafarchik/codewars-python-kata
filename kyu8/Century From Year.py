def century(year):
    cent = int(str(year).zfill(0)[:2])+1
    if year <= 100:
        if year <=100:
            cent=1
    elif year<=1000:
        cent = int(str(year).zfill(0)[:1])+1
    elif year >= 1000:
        year = str(year)
        if year !="":
            if year[3]=="0":
                if year[2]=="0":
                    if year[1]=="0":
                        cent-=1
                    else:
                        cent-=1
    return cent
