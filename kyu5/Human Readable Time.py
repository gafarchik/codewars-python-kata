def make_readable(seconds):
    sec = seconds%60
    min = 0
    hh = 0
    if seconds >=60:
        min = (seconds//60)%60
    if seconds >=3600:
        hh = seconds//3600
    if len(str(sec))==1:
        sec = str("0")+str(sec)
    if len(str(min))==1:
        min = str("0")+str(min)
    if len(str(hh))==1:
        hh = str("0")+str(hh)
    return "{}:{}:{}".format(hh,min,sec)
